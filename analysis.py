import os
from groq import Groq
from test5 import *
from dotenv import load_dotenv
load_dotenv()

def find_theme(reviews):
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        completion = client.chat.completions.create(
            model='llama3-70b-8192',
            messages=[
                {
                    "role": "system", 
                    "content": """Analyze the following Google Reviews and extract the top themes mentioned by customers. Present the output as a numbered list of key themes. For each theme, provide:
                              1. A short title for the theme
                              2. A concise paragraph (2–3 lines max) explaining the theme in natural language, blending key terms and sentiments from the reviews.
                              
                              Do not include the phrase 'Theme explanation:' or any labels before the paragraph. Just the theme title and explanation directly."""
                },
                {
                    "role": "user", 
                    "content": reviews
                }
            ],
            temperature=0.5,
            top_p=1
         )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error"


def find_sentiment_score(message):
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        completion = client.chat.completions.create(
            model='llama3-8b-8192',
            messages=[
                {
                    "role": "system", 
                    "content": """Analyze the sentiment of the following Google Review and its star rating (1-5) and return only a numeric score between -1 (most negative) and +1 (most positive), with 0 being neutral. Do not include any explanations or additional text.
                                  - Combine the text sentiment and star rating.
                                  - Prioritize strong textual cues over ratings. 
                                 Example Inputs & Outputs:
                                 Input:  {'rating': 1.0, 'text':Terrible service! Waited 2 hours and food was cold.}
                                 Output: -1.0
                                 
                                 Input:  {'rating': 3.0, 'text': Good food, but the waiter was rude.}
                                 Output: -0.3
                                 
                                 Input:  {'rating': 5.0, 'text': I’ve had a wonderful experience learning yoga from Rajat Sir. His teaching style is thoughtful and motivating.}
                                 Output: 1.0"""
                },
                {
                    "role": "user", 
                    "content": message
                }
            ],
            temperature=0.1,
            top_p=1
         )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error"

def categorize_sentiment(score):

    if score > 0.33:
        return "positive"
    elif score < -0.33:
        return "negative"
    else:
        return "neutral"

def detect_complaints(reviews):
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        completion = client.chat.completions.create(
            model='llama3-70b-8192',
            messages=[
                {
                    "role": "system", 
                    "content": """You are a customer support assistant. Your job is to read the following Google reviews and identify any that mention complaints or negative experiences. 
                              Return a list of only those reviews that express dissatisfaction, and briefly state what the complaint is about (e.g., bad service, rude staff, poor quality, long wait, etc.)
                              Output Format:
                             - Review: "The coffee was great but the staff seemed inattentive."
                               Issue: "Inattentive staff"

                             - Review: "Terrible service. I had to wait 30 minutes."
                               Issue: "Long wait time and poor service"   """
                },
                {
                    "role": "user", 
                    "content": reviews
                }
            ],
            temperature=0.5,
            top_p=1
         )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error"

