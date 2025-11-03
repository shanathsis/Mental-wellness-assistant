import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sqlite3
import re

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to get a quote for the detected mood
def get_quote(mood):
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT quote FROM quotes WHERE mood=? ORDER BY RANDOM() LIMIT 1", (mood,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "Stay positive! Every day is a chance to grow."

# Comprehensive mood detection function
def detect_mood(user_input):
    user_lower = user_input.lower()
    scores = analyzer.polarity_scores(user_input)
    compound = scores['compound']

    # Sentence patterns for common moods
    sentence_patterns = {
        'sad': [
            r'\b(not|don\'t|do not|isn\'t|is not|can\'t|cannot)\s+.*\s+(good|well|great|fine|okay|ok|alright)\b',
            r'^\s*(feeling|feel|feels)\s+(not)?\s*(good|well|great|fine|okay|ok|bad|terrible|horrible|awful|sick|down|low)\b',
            r'\b(sad|depressed|down|low|unhappy|miserable|hopeless|heartbroken|tearful|broken|hurt|pain|ache)\b',
            r'\b(crying|weeping|devastated|dejected|despondent|melancholy|gloomy)\b',
        ],
        'happy': [
            r'\b(happy|joyful|cheerful|excited|thrilled|delighted|great|amazing|wonderful|fantastic|awesome|brilliant)\b',
            r'\b(feel|feeling|feels)\s+(good|great|wonderful|amazing|awesome|fantastic|excellent|positive|happy|joyful)\b',
        ],
        'angry': [
            r'\b(angry|mad|furious|irritated|annoyed|frustrated|fuming|enraged|rage|livid|seething)\b',
        ],
        'anxious': [
            r'\b(anxious|worried|nervous|stressed|overwhelmed|panicked|uneasy|fearful|scared|terrified|concerned)\b',
        ],
        'exhausted': [
            r'\b(exhausted|tired|fatigued|drained|weary|spent|worn out|burnt out|sleepy|worn)\b',
        ],
        'hopeful': [
            r'\b(hopeful|optimistic|positive|confident|motivated|inspired|determined|focused|driven)\b',
        ],
        'grateful': [
            r'\b(grateful|thankful|blessed|appreciative|lucky|fortunate)\b',
        ],
        'neutral': [
            r'^\s*(okay|ok|fine|alright|neutral|normal)\s*$',
            r'\b(calm|peaceful|serene|balanced|content)\b',
        ],
    }

    # Check sentence patterns first using regex
    for mood, patterns in sentence_patterns.items():
        for pattern in patterns:
            if re.search(pattern, user_lower):
                return mood

    # Fallback to sentiment analysis using VADER scores
    if compound >= 0.05:
        return "happy"
    elif compound <= -0.05:
        # Determine which negative emotion based on additional context
        if 'anxious' in user_lower or 'worried' in user_lower or 'nervous' in user_lower or 'stressed' in user_lower:
            return "anxious"
        elif 'tired' in user_lower or 'exhausted' in user_lower or 'drained' in user_lower:
            return "exhausted"
        else:
            return "sad"
    elif scores['neu'] > 0.8:
        return "neutral"
    else:
        return "neutral"

# Streamlit app layout
st.title("Mental Wellness Assistant")
user_input = st.text_area("Describe how you're feeling today:")

if user_input:
    mood = detect_mood(user_input)
    quote = get_quote(mood)
    st.write(f"**Detected mood:** {mood}")
    st.info(f"💡 Motivational Quote: {quote}")
