# Content-Monetization-Modeler

**Predict YouTube Ad Revenue with Machine Learning**

## Project Overview
The Content Monetization Modeler is a data-driven machine learning project designed to help YouTube creators, advertisers, and media companies estimate and optimize their ad revenue. As digital platforms increasingly rely on advertising for income, creators need predictive insights to guide their content strategy, financial planning, and audience engagement.

This project demonstrates the end-to-end machine learning pipeline, starting from raw data to deployment as an interactive Streamlit web app. It covers exploratory data analysis, data preprocessing, feature engineering, regression modeling, model evaluation, and visualization of insights.

As creators and media companies rely more on platforms like YouTube, **predicting ad revenue** is crucial for content strategy and business planning. This project builds a **machine learning model** to forecast revenue per video based on engagement, audience demographics, and content metadata — and delivers it through an **interactive Streamlit dashboard**.


## table of contents
- [project description](#project-description)


## 🎯 Goal  
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


## 🛠️ Tech Stack  

- [**Python**](https://www.python.org/) – Core programming language for data analysis and modeling  
- [**Pandas**](https://pandas.pydata.org/) – Data manipulation, cleaning, and wrangling  
- [**NumPy**](https://numpy.org/) – Numerical computations and preprocessing  
- [**Scikit-learn**](https://scikit-learn.org/stable/) – Machine learning models, preprocessing, and evaluation  
- [**XGBoost**](https://xgboost.readthedocs.io/) – Gradient boosting model for regression tasks  
- [**Matplotlib**](https://matplotlib.org/) / [**Seaborn**](https://seaborn.pydata.org/) – Data visualization and statistical plots  
- [**Streamlit**](https://streamlit.io/) – Interactive web application for model deployment  
- [**Pickle**](https://docs.python.org/3/library/pickle.html) – Model serialization and saving pipelines  

## ✨ Key Features  

- **Ad Revenue Prediction** – Estimate YouTube video ad revenue based on performance & contextual metrics  
- **Engagement Metrics Analysis** – Study the effect of likes, comments, views, and watch-time on revenue  
- **Feature Engineering** – Create derived features such as engagement rate, revenue per view, etc.  
- **Outlier Detection & Handling** – Identify and treat anomalies in views, revenue, and engagement metrics  
- **Categorical Encoding** – Convert categorical features (category, device, country) into machine-readable format  
- **Exploratory Data Analysis (EDA)** – Revenue distribution plots, correlation heatmaps, and feature importance  
- **Model Comparison** – Evaluate multiple regression models (Linear, Ridge, Lasso, Random Forest, XGBoost)  
- **Interactive Streamlit App** – Input custom video metrics and instantly predict expected ad revenue  
- **Visual Insights Dashboard** – Revenue distribution, feature importance, and correlation visualizations inside the app  


## 📊 Dashboard  

- **Overview**  

  ![Dashboard Overview](https://github.com/vinozzxx/Content-Monetization-Modeler/blob/9304af28e53c9a5977a0a13a6adf85369c685521/dashboard_1.png)

- **Prediction Output**  

  ![Prediction Output](assets/dashboard_prediction.png)  


















  
