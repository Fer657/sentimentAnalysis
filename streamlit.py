import streamlit as st
import pandas as pd
import pickle

# Set the background image and opacity
background_image_url = "E:\pds\frontend\pacifistaimagen_K2Cfkcj.width-800.jpg"  

background_html = f"""
<style>
    body {{
        background-image: url("https://i.imgur.com/jcJEMo8.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        opacity: 0.5; /* 50% transparency */
    }}
</style>
"""

def knn_model(text):
    with open(r"knn_model.pkl", "rb") as file:
        knn = pickle.load(file)
    with open(r"tfidf.pkl", "rb") as file:
        tfidf = pickle.load(file)
    tf = tfidf.transform([text])
    sentiment = knn.predict(tf)

    return sentiment


def nb_model(text):
    with open(r"naives_model.pkl", "rb") as file:
        nb = pickle.load(file)
    with open(r"tfidf.pkl", "rb") as file:
        tfidf = pickle.load(file)
    tf = tfidf.transform([text])
    sentiment = nb.predict(tf)

    return sentiment


# NAV BAR
rad = st.sidebar.selectbox("Navigation", ["Home", "Knn Classifier", "Naive Bayes Classifier", "EDA", "Workflow"])

# HOME PAGE
if rad == "Home":
    st.write(background_html, unsafe_allow_html=True)
    st.title("Sentiment Analysis")

# KNN CLASSIFIER
elif rad == "Knn Classifier":
    st.header("KNN Classifier")
    table_data = {
    'Metrics': ['Precision', 'Recall', 'F1-Score', 'Support'],
    'Negative': [0.71, 0.64, 0.68, 337],
    'Neutral': [0.85, 0.14, 0.24, 168],
    'Positive': [0.60, 0.86, 0.71, 392],
    'Accuracy': [0.64, '', '', 897],
    'Macro Avg': [0.72, 0.55, 0.54, 897],
    'Weighted Avg': [0.69, 0.64, 0.61, 897]}
    df = pd.DataFrame(table_data)
    st.write(df)

    with st.expander('Analyze Text'):
        text = st.text_input('Text here: ')
        sentiment = knn_model(text)
        st.write(f"The sentiment of text: {sentiment}")
    # knn calling

    with st.expander('Analyze CSV'):
        upl = st.file_uploader('Upload file')
        if upl:
            data = pd.read_csv(upl)
            df = pd.DataFrame(data)
            size = len(data)
            sentiments = []

            for i in range(size):
                sentiment = knn_model(df.loc[i, "text"])# Make a prediction using your model
                sentiments.append(sentiment)

            data['Sentiment'] = sentiments
            st.dataframe(data)

# NAIVE BAYES
elif rad == "Naive Bayes Classifier":
    st.header("Naive Bayes Classifier")
    table_data = {
    'Metrics': ['Precision', 'Recall', 'F1-Score', 'Support'],
    'Negative': [0.71, 0.64, 0.68, 337],
    'Neutral': [0.85, 0.14, 0.24, 168],
    'Positive': [0.60, 0.86, 0.71, 392],
    'Accuracy': [0.64, '', '', 897],
    'Macro Avg': [0.72, 0.55, 0.54, 897],
    'Weighted Avg': [0.69, 0.64, 0.61, 897]}
    df = pd.DataFrame(table_data)
    st.write(df,index = False)
    with st.expander('Analyze Text'):
        text = st.text_input('Text here: ')
    

    with st.expander('Analyze CSV'):
        upl =st.file_uploader('Upload file')
        if upl:
            data = pd.read_csv(upl)
            df = pd.DataFrame(data)
            size = len(data)
            sentiments = []

            for i in range(size):
                sentiment = nb_model(df.loc[i, "text"])# Make a prediction using your model
                sentiments.append(sentiment)

            data['Sentiment'] = sentiments
            st.dataframe(data)

# EDA
elif rad == "EDA":
    st.header("Exploratory Data Analysis")

# FLOWCHART
else:
    st.header("Workflow Diagram")
