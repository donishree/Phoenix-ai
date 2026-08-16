import streamlit as st
import pandas as pd
import joblib

model = joblib.load("phoenix_ai_model.pkl")

st.title("Phoenix AI - Webpage Decline Risk Predictor")
st.write("Upload your webpage search performance data to check risk levels.")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, sep=";", decimal=",")
    st.write("Preview of your data:")
    st.dataframe(data.head())

    feature_cols = ["Clicks", "Impressions", "Position", "Title Length",
                     "Meta Description Length", "H1 Length", "Word Count",
                     "Sentence Count", "Folder Depth", "Link Score",
                     "Inlinks", "Outlinks", "Response Time"]

    missing_cols = [col for col in feature_cols if col not in data.columns]

    if missing_cols:
        st.error(f"Your file is missing these required columns: {missing_cols}")
    else:
        predictions = model.predict(data[feature_cols])
        probabilities = model.predict_proba(data[feature_cols])
        confidence = probabilities.max(axis=1)

        data["Predicted_Risk"] = predictions
        data["Confidence"] = (confidence * 100).round(1)

        def recommend(row):
            reasons = []
            if row["Position"] > 20:
                reasons.append("poor search position")
            if row["Word Count"] < data["Word Count"].median():
                reasons.append("below-average content length")
            if not reasons:
                return "No urgent action needed. Monitor periodically."
            return "Review: " + "; ".join(reasons) + "."

        data["Recommendation"] = data.apply(recommend, axis=1)

        st.write("Predictions:")
        st.dataframe(data[["Predicted_Risk", "Confidence", "Recommendation"] + feature_cols])