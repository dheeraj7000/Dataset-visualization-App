import streamlit as st
import pandas as pd
import plotly.express as px
from pandas_profiling import ProfileReport
from io import StringIO, BytesIO
import altair as alt
import base64

# App configuration
st.set_page_config(
    page_title="DataViz Explorer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load custom CSS
local_css("style.css")

# App header
st.title("📊 DataViz Explorer")
st.markdown("""
    <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin-bottom:20px;">
    <h2 style="color:white;text-align:center;">Upload your dataset and get instant visualizations and EDA reports</h2>
    </div>
""", unsafe_allow_html=True)

# Sidebar for file upload and settings
with st.sidebar:
    st.header("Upload & Settings")
    
    # File uploader with multiple format support
    uploaded_file = st.file_uploader(
        "Choose a file (CSV, Excel, JSON)",
        type=["csv", "xlsx", "xls", "json", "parquet"]
    )
    
    st.markdown("---")
    st.subheader("Visualization Settings")
    chart_type = st.selectbox(
        "Select chart type",
        ["Scatter", "Line", "Bar", "Histogram", "Box", "Violin", "Pie"]
    )
    st.markdown("---")
    st.markdown("""
        <div style="text-align:center;padding:10px;background-color:#464e5f;border-radius:10px;">
            <p style="color:white;">Made with ❤️ using Streamlit</p>
        </div>
    """, unsafe_allow_html=True)

# Main content area
if uploaded_file is not None:
    try:
        # Read the file based on its extension
        file_extension = uploaded_file.name.split(".")[-1].lower()
        
        if file_extension == "csv":
            df = pd.read_csv(uploaded_file)
        elif file_extension in ["xlsx", "xls"]:
            df = pd.read_excel(uploaded_file)
        elif file_extension == "json":
            df = pd.read_json(uploaded_file)
        elif file_extension == "parquet":
            df = pd.read_parquet(uploaded_file)
        else:
            st.error("Unsupported file format")
        
        # Display the dataframe
        st.subheader("Uploaded Data Preview")
        st.dataframe(df.head())
        
        # Show basic info
        st.subheader("Data Information")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info(f"Rows: {df.shape[0]}")
        with col2:
            st.info(f"Columns: {df.shape[1]}")
        with col3:
            st.info(f"Missing Values: {df.isna().sum().sum()}")
        
        # Visualization section
        st.markdown("---")
        st.subheader("Interactive Visualization")
        
        # Select columns for visualization
        cols = df.columns.tolist()
        x_axis = st.selectbox("Select X-axis", cols, index=0)
        y_axis = st.selectbox("Select Y-axis", cols, index=1 if len(cols) > 1 else 0)
        color_col = st.selectbox("Select Color (optional)", [None] + cols)
        
        # Create the selected chart
        if chart_type == "Scatter":
            fig = px.scatter(df, x=x_axis, y=y_axis, color=color_col, 
                             title=f"Scatter Plot: {x_axis} vs {y_axis}")
        elif chart_type == "Line":
            fig = px.line(df, x=x_axis, y=y_axis, color=color_col,
                          title=f"Line Chart: {x_axis} vs {y_axis}")
        elif chart_type == "Bar":
            fig = px.bar(df, x=x_axis, y=y_axis, color=color_col,
                         title=f"Bar Chart: {x_axis} vs {y_axis}")
        elif chart_type == "Histogram":
            fig = px.histogram(df, x=x_axis, color=color_col,
                              title=f"Histogram: {x_axis}")
        elif chart_type == "Box":
            fig = px.box(df, x=x_axis, y=y_axis, color=color_col,
                         title=f"Box Plot: {x_axis} vs {y_axis}")
        elif chart_type == "Violin":
            fig = px.violin(df, x=x_axis, y=y_axis, color=color_col,
                            title=f"Violin Plot: {x_axis} vs {y_axis}")
        elif chart_type == "Pie":
            fig = px.pie(df, names=x_axis, values=y_axis, 
                         title=f"Pie Chart: {x_axis}")
        
        # Display the chart
        st.plotly_chart(fig, use_container_width=True)
        
        # EDA Report section
        st.markdown("---")
        st.subheader("Exploratory Data Analysis Report")
        
        with st.spinner("Generating EDA report..."):
            profile = ProfileReport(df, explorative=True)
            
            # Show the report in the app
            st_profile_report(profile)
            
            # Add download button for the report
            profile_html = profile.to_html()
            b64 = base64.b64encode(profile_html.encode()).decode()
            href = f'<a href="data:text/html;base64,{b64}" download="eda_report.html">Download Full EDA Report</a>'
            st.markdown(href, unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

else:
    st.info("Please upload a file to get started")
    st.image("https://cdn.pixabay.com/photo/2017/08/06/22/01/upload-2598373_1280.jpg", 
             use_column_width=True)

# Custom function to display pandas profiling report in Streamlit
def st_profile_report(pr):
    import streamlit.components.v1 as components
    pr_html = pr.to_html()
    components.html(pr_html, height=1000, scrolling=True)
