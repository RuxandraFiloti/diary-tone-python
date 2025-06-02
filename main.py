import glob
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

st.header("Diary Tone")

st.subheader("Positive")



#sorted list
filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()


negativity = []
positivity = []

#analyzing
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

#extrating the dates
dates = [name.strip(".txt").strip("diary/") for name in filepaths]

pos_figure = px.line(x=dates, y=positivity, labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negative")

neg_figure = px.line(x=dates, y=negativity, labels={"x":"Dates", "y":"Negativity"})
st.plotly_chart(neg_figure)
