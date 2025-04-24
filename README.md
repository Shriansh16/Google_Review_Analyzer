# Google Review Analyzer

## Overview
The Google Review Analyzer is an AI application that helps businesses and analysts extract meaningful insights from Google reviews. It provides sentiment analysis, identifies key themes, detects complaints, and visualizes review trends for any business listed on Google.

## Live Demo
- Access the deployed application here: https://businessreviewanalyzer.streamlit.app/    
- Access the demo video here: https://drive.google.com/file/d/10Q0yIvzNy_zUVh8zCm9ZLbVc0Jv0H3rm/view?usp=sharing                     
- Short write-up: https://drive.google.com/file/d/1guwU2QyrapnVKm6uQpHLlc8a7v1WGeuX/view?usp=sharing                                                             

## Features
- Business Search: Find any business by name

- Review Analysis: Analyze up to 50 most recent reviews

- Sentiment score trend visualization

- Sentiment category distribution (positive/neutral/negative)

- Theme Extraction: Identifies key themes in customer feedback

- Complaint Detection: Highlights specific customer complaints and issues

## How It Works
1. Data Collection
The application uses the SerpAPI to:

- Search for businesses by name and retrieve their unique data_id

- Fetch the most recent reviews (up to 50) for the business

2. Analysis Pipeline
- The collected reviews are processed through several AI-powered analysis steps:

- Theme Extraction: Uses Groq's Llama3-70b model to identify and summarize key themes

- Sentiment Scoring: Uses Llama3-8b to assign sentiment scores (-1 to +1) to each review

- Complaint Detection: Uses Llama3-70b to identify and extract specific complaints

3. Visualization
The results are presented through:

- Line charts showing sentiment trends

- Pie charts showing sentiment distribution

## Usage
1. Enter the full name of a business in the search box (enter the exact name as it appears on Google Maps).

2. Click "Submit"

3. View the analysis results including:

 - Key themes in customer feedback

 - Sentiment score trend over time

 - Sentiment distribution (positive/neutral/negative)

 - Specific customer complaints detected