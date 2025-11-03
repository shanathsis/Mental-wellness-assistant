# Mental-wellness-assistant
This project is a Mood-Based Mental Wellness Assistant web application built with Streamlit, VADER Sentiment Analysis, and SQLite. Users describe their feelings, and the app intelligently detects their mood using advanced sentiment analysis and custom pattern matching. It then returns a motivational quote from a database that matches the user's detected emotional state.

Features
Advanced Mood Detection: Combines VADER Sentiment Intensity Analyzer with regex-based pattern matching for accurate mood classification.

Motivational Quotes: Fetches relevant quotes from an SQLite database according to the user's mood for personalized encouragement.

Simple, Interactive UI: Powered by Streamlit, allowing seamless user interaction and immediate feedback.

Easy to Customize: Add or modify moods, sentence patterns, and quotes to suit different wellness needs.

Technologies Used
Python (Streamlit)

VADER SentimentIntensityAnalyzer

SQLite

Usage
Run the app locally with:

text
streamlit run app.py
Enter a description of your feelings in the text box.

The app will display your detected mood and an inspirational quote.

Ideal For
Mental health advocates

Self-care platforms

Personal wellness websites

Anyone seeking a simple, customizable emotional support tool

Repository Content
app.py — Main application script

quotes.db — SQLite database of motivational quotes organized by mood

This project provides a warm, supportive, and personalized user experience for daily emotional check-ins.
