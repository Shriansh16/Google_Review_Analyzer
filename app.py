import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from test5 import *
from analysis import *

st.set_page_config(page_title="Google Review Analyzer", page_icon="🔍", layout="centered")
st.title("🔍 Google Review Analyzer")
st.markdown("Enter the full name of a business below to analyze its recent Google reviews 💬")

business_name = st.text_input("E.g. Starbucks Mumbai CST", placeholder="Type the business name here...")

if st.button("Submit"):
    if business_name:
        with st.spinner("Analyzing reviews..."):
            data_id = get_place_data_id(business_name)
            if not data_id:
                st.error("❌ Business not found. Please check the name and try again.")
                st.stop()
            reviews = get_reviews_from_data_id(data_id, 50)
            reviews_str = str(reviews)
            st.subheader("🧠 Key Themes in Customer Feedback")
            st.write(find_theme(reviews_str))
            sentiment_scores = [float(find_sentiment_score(str(review))) for review in reviews]
            categories = [categorize_sentiment(score) for score in sentiment_scores]
            st.subheader("📈 Sentiment Score Trend (Most Recent to Oldest)")
            df_scores = pd.DataFrame({
                'Review Index': list(range(len(sentiment_scores))),
                'Sentiment Score': sentiment_scores
            })
            st.line_chart(df_scores.set_index('Review Index'))

            # Pie Chart: Sentiment Category Distribution
            st.subheader("🥧 Sentiment Distribution")
            df_categories = pd.Series(categories).value_counts()
            fig, ax = plt.subplots()
            ax.pie(df_categories, labels=df_categories.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
            ax.axis('equal')
            st.pyplot(fig)
            st.subheader("🚨 Customer Complaints & Issues Detected")
            st.write(detect_complaints(reviews_str))
