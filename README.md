# Content Monetization Modeler

**Predict YouTube Ad Revenue with Machine Learning**

## Project Overview
The Content Monetization Modeler is a data-driven machine learning project designed to help YouTube creators, advertisers, and media companies estimate and optimize their ad revenue. As digital platforms increasingly rely on advertising for income, creators need predictive insights to guide their content strategy, financial planning, and audience engagement.

This project demonstrates the end-to-end machine learning pipeline, starting from raw data to deployment as an interactive Streamlit web app. It covers exploratory data analysis, data preprocessing, feature engineering, regression modeling, model evaluation, and visualization of insights.

As creators and media companies rely more on platforms like YouTube, **predicting ad revenue** is crucial for content strategy and business planning. This project builds a **machine learning model** to forecast revenue per video based on engagement, audience demographics, and content metadata — and delivers it through an **interactive Streamlit dashboard**.


## table of contents
- [project description](#project-description)
- [dataset insight](#dataset-insight)
- [tech stack](#tech-stack)
- [key features](#key-features)
- [documentation](#documentation)
- [dashboard](#dashboard)
- [project structure](#project-structure)
- [faqs](#faqs)


## Goal  
The primary goal of the **Content Monetization Modeler** is to **predict YouTube ad revenue** for individual videos using machine learning models, and make the results accessible via an interactive **Streamlit app**.  

This enables content creators and media companies to:  
- Forecast expected ad revenue for upcoming videos.  
- Identify which content features (views, watch time, engagement, etc.) drive monetization.  
- Use data-driven insights to improve **content strategy and revenue planning**.  

## 📊 Dataset Insight  
The dataset contains daily performance and contextual information for YouTube videos, including:  

- **Video ID** – Unique identifier for each video  
- **Date** – Upload/reporting date  
- **Views** – Number of video views  
- **Likes & Comments** – Engagement metrics from viewers  
- **Watch Time (minutes)** – Total time spent watching  
- **Video Length (minutes)** – Duration of the video  
- **Subscribers** – Channel’s subscriber count at the time  
- **Category** – Content category (e.g., Tech, Music, Gaming)  
- **Device** – Platform used (Mobile, Desktop, TV, etc.)  
- **Country** – Viewer’s geographical location  
- **Ad Revenue (USD)** – Target variable, representing daily ad revenue earned

**[`^        back to top        ^`](#Content-Monetization-Modeler)**

## Tech Stack  

- [**Python**](https://www.python.org/) – Core programming language for data analysis and modeling  
- [**Pandas**](https://pandas.pydata.org/) – Data manipulation, cleaning, and wrangling  
- [**NumPy**](https://numpy.org/) – Numerical computations and preprocessing  
- [**Scikit-learn**](https://scikit-learn.org/stable/) – Machine learning models, preprocessing, and evaluation  
- [**XGBoost**](https://xgboost.readthedocs.io/) – Gradient boosting model for regression tasks  
- [**Matplotlib**](https://matplotlib.org/) / [**Seaborn**](https://seaborn.pydata.org/) – Data visualization and statistical plots  
- [**Streamlit**](https://streamlit.io/) – Interactive web application for model deployment  
- [**Pickle**](https://docs.python.org/3/library/pickle.html) – Model serialization and saving pipelines  

## Key Features  

- **Ad Revenue Prediction** – Estimate YouTube video ad revenue based on performance & contextual metrics  
- **Engagement Metrics Analysis** – Study the effect of likes, comments, views, and watch-time on revenue  
- **Feature Engineering** – Create derived features such as engagement rate, revenue per view, etc.  
- **Outlier Detection & Handling** – Identify and treat anomalies in views, revenue, and engagement metrics  
- **Categorical Encoding** – Convert categorical features (category, device, country) into machine-readable format  
- **Exploratory Data Analysis (EDA)** – Revenue distribution plots, correlation heatmaps, and feature importance  
- **Model Comparison** – Evaluate multiple regression models (Linear, Ridge, Lasso, Random Forest, XGBoost)  
- **Interactive Streamlit App** – Input custom video metrics and instantly predict expected ad revenue  
- **Visual Insights Dashboard** – Revenue distribution, feature importance, and correlation visualizations inside the app  

**[`^        back to top        ^`](#Content-Monetization-Modeler)**

## Dashboard  

- **Overview**  

  ![Dashboard Overview](https://github.com/vinozzxx/Content-Monetization-Modeler/blob/9304af28e53c9a5977a0a13a6adf85369c685521/dashboard_1.png)

- **Prediction Output**  

  ![Prediction Output](https://github.com/vinozzxx/Content-Monetization-Modeler/blob/8fdaf7462b798658cc81c00fd08b09ec122e5080/dashboard_2.png)  

**[`^        back to top        ^`](#Content-Monetization-Modeler)**

The dashboard includes the following insights:  

- **Input Controls** – Users can enter video metrics (views, likes, comments, watch time, subscribers) along with metadata (upload date, category, device, country).  
- **KPI Card** – Displays the **predicted revenue** for the video in a highlighted box.  
- **Summary Panel** – Shows the entered metrics and metadata for easy verification.  
- **Comparison Visuals** *(optional)* – Feature importance plots and revenue distribution graphs from the training pipeline help understand model behavior.  
- **Interactive Workflow** – Real-time prediction powered by the trained XGBoost pipeline.  


## Project Structure
```
📁 Content-Monetization-Modeler/
│
├── 📄 main.py # Full pipeline: EDA → Preprocessing → Modeling
├── 📄 app.py # Streamlit dashboard for revenue prediction
├── 📄 youtube_data.csv # Dataset (synthetic YouTube video stats)
│
├── 📂 models/ # Saved ML pipelines & scalers
│ ├── pipe_xgb.pkl # Trained XGBoost pipeline
│ └── y_scaler.pkl # Target scaler for inverse transform
│
├── 📂 assets/ # Visualization outputs
│ ├── revenue_distribution.png
│ ├── correlation_heatmap.png
│ └── feature_importance.png
│
├── 📄 requirements.txt # Project dependencies
└── 📄 README.md # Documentation

```
**[`^        back to top        ^`](#Content-Monetization-Modeler)**

## FAQs  

1. `What is this project about?`  
A machine learning project that predicts **YouTube ad revenue for videos** based on engagement and metadata features. It includes an **end-to-end pipeline** with EDA, preprocessing, model building, and a Streamlit app for deployment.  

2. `What insights are provided?`  
- Feature importance for revenue prediction  
- Correlation between engagement metrics (views, likes, comments, watch-time) and ad revenue  
- Model comparison across ML algorithms (Linear Regression, Random Forest, XGBoost)  
- Prediction of expected ad revenue for new video data  

3. `What technologies are used?`  
- [**Python**](https://www.python.org/) – Core development  
- [**Pandas**](https://pandas.pydata.org/) – Data cleaning & wrangling  
- [**NumPy**](https://numpy.org/) – Numerical computations  
- [**Scikit-learn**](https://scikit-learn.org/) – Machine learning pipelines  
- [**XGBoost**](https://xgboost.readthedocs.io/) – Gradient boosting for accurate predictions  
- [**Matplotlib**](https://matplotlib.org/) / [**Seaborn**](https://seaborn.pydata.org/) – Visualization  
- [**Streamlit**](https://streamlit.io/) – Interactive web app for predictions  

4. `How to run the project?`

```bash
git clone [https://github.com/your-username/Content-Monetization-Modeler.git](https://github.com/your-username/Content-Monetization-Modeler.git)
cd Content-Monetization-Modeler
pip install -r requirements.txt
streamlit run app.py
```
5. `Can I contribute?`
Yes! Fork the repo, make your changes, and raise a pull request. All contributions are welcome 🚀


**[`^        back to top        ^`](#Content-Monetization-Modeler)**











  
