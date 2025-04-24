# 📊 DataViz Explorer

**A beautiful web app for automated data visualization and exploratory data analysis (EDA)**

![App Screenshot](https://i.imgur.com/JQ8w0Yn.png)

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)

## 🚀 Features

- **Multi-format support**: Upload CSV, Excel, JSON, or Parquet files
- **Interactive Visualizations**: 
  - Scatter, Line, Bar, Histogram, Box, Violin, and Pie charts
  - Fully customizable axes and colors
  - Zoom, pan, and hover interactions
- **Automated EDA Reports**:
  - Complete statistical summary
  - Correlation analysis
  - Missing values detection
  - Downloadable HTML report
- **Beautiful UI**:
  - Modern, responsive design
  - Dark/light mode compatible
  - Informative data metrics cards

## 🛠️ Installation

1. Clone the repository:
```bash
  git clone https://github.com/yourusername/data-viz-explorer.git
  cd data-viz-explorer
```

2. Create and activate a virtual environment:
```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
  pip install -r requirements.txt
```

## 🏃 Running the App

```bash
  streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 🌐 Deployment

### Streamlit Sharing (Recommended)
1. Push your code to GitHub
2. Sign up at [Streamlit Sharing](https://share.streamlit.io/)
3. Click "New App" and connect your repository

### Heroku
```bash
heroku create your-app-name
git push heroku main
```

## 📸 Screenshots

| Data Preview | Interactive Visualization | EDA Report |
|-------------|--------------------------|------------|
| ![Data Preview](https://i.imgur.com/5XQZz9p.png) | ![Visualization](https://i.imgur.com/JQ8w0Yn.png) | ![EDA Report](https://i.imgur.com/8GtVQ3s.png) |

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Data Processing**: Pandas
- **Visualization**: Plotly, Altair
- **EDA**: Pandas-profiling

## 📂 File Structure

```
data-viz-explorer/
├── app.py                # Main application code
├── style.css             # Custom CSS styles
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── .gitignore            # Git ignore file
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## ✉️ Contact

Dheeraj Kumar  - 13kumardheeraj@gmail.com

Project Link: [PROJECT LINK](https://github.com/dheeraj7000/Dataset-visualization-App)
