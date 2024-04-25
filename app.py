import streamlit as st
from transformers import pipeline

classifier = pipeline("sentiment-analysis")   # Load sentiment analysis model

st.title("Sentiment Analysis")
text = st.text_input("Enter a sentence")

if st.button("Analyze Sentiment"):
    if text:
        results = classifier([text])
        for result in results:
            st.write(f"It seems you have entered something {result['label']}. That is a {result['label']} SENTIMENT")
            st.write(f"Score: {round(result['score'], 4)}")

    else:
        st.warning("Please enter some text")


