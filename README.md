<h1 align="center">Simple sentiment analysis app</h1>

<p align="center">
  <a href="https://greenai-report.streamlit.app/">
    <img src="https://img.shields.io/badge/Deployed%20on-Streamlit-red?logo=streamlit">
  </a>
  <a href="https://www.nltk.org/">
    <img src="https://img.shields.io/badge/NLTK-Powered-blue?logo=python">
  </a>
</p>


### Installation
To run the app you need to have installed:

- streamlit
- nltk


### Sentiment analysis
Sentiment analysis by NLTK

```python
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
sentiment_scores = sid.polarity_scores(input_text)
```




