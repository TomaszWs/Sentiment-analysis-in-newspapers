# Sentiment-analysis-in-newspapers
Program is meant to analyse the sentiment in newspapers using NLTK library.
## Current version
Program analyses an article _Biden admin's plan for mass release of migrants into US outlined in internal 2022 memo_ from the Fox News. The text is tokenised, lemmatised, stripped of non-alphabetic characters. Then, stopwords (for example articles) are removed from the list of tokens. After that the list of tokens is merged and analysed using Sentiment Intensity Analyzer. Results are saved in new files.
### Analysis by sentences
Additionally, the input is analysed by sentences (whole sentences are treated as tokens)