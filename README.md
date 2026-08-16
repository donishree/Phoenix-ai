# 🦅 Phoenix AI

## Explainable Machine Learning for Webpage Performance Decline Risk

Phoenix AI is a machine learning system that analyzes webpage and search-performance signals to identify pages that may require content optimization.

The project was developed as an extension of my Phoenix AI research work from the FlyRank AI Fluency Internship capstone.

The system combines:

- Search-performance data analysis
- Machine learning classification
- Model explainability
- Rule-based recommendations
- A deployed Streamlit application

---

## 🎯 Project Goal

The goal of Phoenix AI is to help identify webpages that may need optimization by analyzing observable search-performance signals.

The system classifies webpages into three risk categories:

- 🟢 **Stable**
- 🟡 **At Risk**
- 🔴 **Declining**

The prediction is accompanied by confidence information and rule-based recommendations for possible content optimization actions.

---

## 📊 Dataset

Because the original FlyRank internship dataset was not available, Phoenix AI uses a real public Kaggle dataset:

**Real Website Traffic Prediction**

The dataset contains:

- **9,439 rows**
- **19 original columns**

It includes Google Search Console-style performance signals such as:

- Clicks
- Impressions
- Search Position

along with content-related features such as:

- Word Count
- Title Length
- Inlinks
- and other webpage attributes.

---

## 🧹 Data Preparation

During preprocessing:

- 5 columns with approximately 82% missing values were removed.
- Remaining numeric missing values were handled using median imputation.
- The final cleaned dataset contained **9,439 rows and 14 columns**.

The preprocessing stage was performed before model training.

---

## 🔍 Exploratory Data Analysis

The dataset was analyzed to understand the underlying patterns.

Key observations included:

- Clicks are heavily right-skewed.
- Impressions are heavily right-skewed.
- Search Position shows an expected relationship with Clicks.
- Search-performance signals provide useful information for distinguishing different webpage risk categories.

---

## 🎯 Target Definition

The dataset does not contain historical time-series information showing how an individual webpage changes over time.

Therefore, Phoenix AI does **not** claim to directly measure literal webpage decline over time.

Instead, a proxy target called `Risk_Label` was created.

The label compares each webpage's Click-Through Rate (CTR) with the median CTR of webpages in a similar Search Position bucket.

The resulting categories are:

- **Stable**
- **At Risk**
- **Declining**

This is an explicit modeling assumption and should be interpreted as **performance-risk classification**, rather than direct longitudinal decline prediction.

---

## 🤖 Machine Learning Models

Two models were trained and evaluated.

### Logistic Regression

Logistic Regression was used as the baseline classification model.

**Accuracy: 56%**

This baseline provided a reference point for evaluating the more interpretable tree-based model.

### Decision Tree

A Decision Tree was trained using:

- `max_depth = 5`
- `class_weight = "balanced"`

The Decision Tree achieved:

**Accuracy: 94%**

Class-level F1 scores:

| Class | F1-Score |
|---|---:|
| Stable | 0.96 |
| Declining | 0.99 |
| At Risk | 0.22 |

The low F1-score for the At Risk class is important because this class contains substantially fewer examples than the other classes.

---

## ⚖️ Class Distribution

The target distribution was imbalanced:

| Risk Category | Samples |
|---|---:|
| Stable | 8,092 |
| Declining | 1,262 |
| At Risk | 85 |

Because the At Risk class contains only a small number of samples, its predictions require additional caution.

This class imbalance is treated as an important limitation of the current model.

---

## 🧠 Explainability

Explainability is a core part of Phoenix AI.

The Decision Tree feature importance analysis showed that the model's predictions were primarily influenced by:

| Feature | Approximate Importance |
|---|---:|
| Position | 47% |
| Impressions | 38% |
| Clicks | 15% |

These values describe the features the trained model relied on most heavily.

They should not be interpreted as proof that these variables independently cause webpage decline.

---

## 💡 Recommendation Layer

Phoenix AI includes a separate **rule-based recommendation layer**.

The recommendations are NOT generated directly by the machine learning model.

The system can flag situations such as:

- Poor search position
- High impressions combined with low CTR
- Thin content

Based on these signals, the system provides possible content optimization actions.

This separation keeps the machine learning prediction and recommendation logic transparent.

---

## 🏗️ System Workflow

```text
Webpage/Search Performance Data
              ↓
       Data Preprocessing
              ↓
     Feature Engineering
              ↓
        Risk Labeling
              ↓
        Train/Test Split
              ↓
      Machine Learning Model
              ↓
       Risk Classification
              ↓
         Explainability
              ↓
   Rule-Based Recommendations
              ↓
        Phoenix AI Output

🌐 Live Application

Phoenix AI has been deployed as a Streamlit web application.

Users can upload a CSV file and receive:

Risk predictions
Confidence scores
Feature-based insights
Content optimization recommendations
🚀 Try Phoenix AI

Open the Live Phoenix AI Application

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Joblib
Streamlit
Git
GitHub
📁 Project Structure
Phoenix-ai/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
├── notebooks/
├── models/
├── reports/
└── screenshots/
🚀 Running the Project Locally

Clone the repository:

git clone https://github.com/donishree/Phoenix-ai.git

Move into the project directory:

cd Phoenix-ai

Install the required dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

The application will then open in your browser.

⚠️ Limitations
1. Proxy Target

The dataset does not contain time-series information.

Therefore, the Risk_Label represents a performance-risk proxy rather than direct measurement of decline over time.

2. Class Imbalance

The At Risk category contains only 85 examples compared with thousands of Stable examples.

Consequently, the model performs much less reliably on this minority class.

3. Dataset Scope

The model is trained on a public dataset rather than the original FlyRank internship dataset.

Therefore, its results should not be interpreted as evidence of performance on FlyRank's internal data.

4. Recommendations

The recommendation system is rule-based rather than learned by the ML model.

5. Generalization

The model should be tested on additional datasets before being treated as a production-grade webpage optimization system.

🔮 Future Work

Future versions of Phoenix AI could include:

Real longitudinal Google Search Console data
More diverse webpage datasets
Better representation of the At Risk class
Time-series decline prediction
Additional machine learning models
More advanced explainability
Automated content recommendations
Historical performance monitoring
Model retraining pipelines
Larger-scale production deployment
👩‍💻 Author

Donishree

B.Tech Computer Science and Engineering — Artificial Intelligence & Machine Learning

📌 Project Context

Phoenix AI was developed as an extension of my AI Fluency internship capstone work at FlyRank, evolving the original research concept into an implemented machine learning pipeline and deployed application.

🔗 Project Links

GitHub:
https://github.com/donishree/Phoenix-ai

Live Application:
https://phoenix-ai-hvoomxgzvzme8fk2ymw52b.streamlit.app/
