import streamlit as st
import nltk
import plotly.express as px
# Download required NLTK model
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Function to analyze sentiment and return the dominant sentiment with emoji
def sentiment_analysis(input_text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(input_text)

    # Determine the most impactful sentiment
    sentiment = max(sentiment_scores, key=lambda k: sentiment_scores[k] if k != "compound" else -1)

    # Map sentiment to emoji and labels
    sentiment_emoji = {
        "pos": "😃",
        "neg": "😞",
        "neu": "😐"
    }
    sentiment_text = {
        "pos": "Positive",
        "neg": "Negative",
        "neu": "Neutral"
    }

    return sentiment_emoji.get(sentiment, "🤔"), sentiment_text.get(sentiment, "Unknown"), sentiment_scores

# Function to generate an interactive Plotly chart
def plot_sentiment_scores(sentiment_scores):
    scores_df = {
        "Sentiment": list(sentiment_scores.keys()),
        "Score": list(sentiment_scores.values())
    }

    # Create a Plotly bar chart
    fig = px.bar(scores_df, x="Sentiment", y="Score", 
                 title="Sentiment Score Breakdown", 
                 color="Sentiment", text="Score")

    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')

    return fig

# Streamlit app layout
st.title("Sentiment Analysis App")

# State variables for output
if "output_text" not in st.session_state:
    st.session_state.output_text = ""
if "output_emoji" not in st.session_state:
    st.session_state.output_emoji = ""
if "output_sentiment" not in st.session_state:
    st.session_state.output_sentiment = ""
if "sentiment_scores" not in st.session_state:
    st.session_state.sentiment_scores = None

# Centered Output Display
st.markdown(
    f"""
    <div style="text-align: center; font-size: 50px;">
        {st.session_state.output_emoji}
    </div>
    <div style="text-align: center; font-size: 24px; font-weight: bold;">
        {st.session_state.output_sentiment}
    </div>
    """,
    unsafe_allow_html=True
)

# User input field
user_input = st.text_input("Enter sentiment:")

# Button to trigger sentiment analysis
if st.button("Submit"):
    emoji, sentiment, scores = sentiment_analysis(user_input)
    st.session_state.output_emoji = emoji
    st.session_state.output_sentiment = sentiment
    st.session_state.sentiment_scores = scores
    st.rerun()  # Refresh UI

# Display Plotly Sentiment Score Plot (only if scores exist)
if st.session_state.sentiment_scores:
    st.write("### Sentiment Score Breakdown:")

    # Show the interactive Plotly chart
    fig = plot_sentiment_scores(st.session_state.sentiment_scores)
    st.plotly_chart(fig, use_container_width=True)
