<h1 align="center">Simple sentiment analysis app</h1>

<p align="center">
  <a href="https://simple-sentiment-analysis.streamlit.app/">
    <img src="https://img.shields.io/badge/Deployed%20on-Streamlit-red?logo=streamlit">
  </a>
  <a href="https://www.nltk.org/">
    <img src="https://img.shields.io/badge/NLTK-Powered-blue?logo=python">
  </a>
</p>


### Set up
Requirements:
- python v.3.10.6

To install the app run the following command:

```sh
pip install -r requirements.txt
```

To run the app run the following command:

```sh
streamlit run app.py
```


### Sentiment analysis
Sentiment analysis by NLTK

```python
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
sentiment_scores = sid.polarity_scores(input_text)
```




