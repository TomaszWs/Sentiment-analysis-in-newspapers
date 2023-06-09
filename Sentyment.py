import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize

# nltk.download('stopwords')
# nltk.download('punkt') #moduł do tokenizacji etc.
# nltk.download('vader_lexicon')
# nltk.download('wordnet')

def processing(tekst):
    tokens = word_tokenize(tekst.lower())
    lemmatyzacja = WordNetLemmatizer()
    tokens_lemma = [lemmatyzacja.lemmatize(token) for token in tokens]
    tokens_without = [token for token in tokens_lemma if token.isalpha()]
    stop_words = set(stopwords.words('english')) #nazwa nie może być stopwords, żeby się nie pokrywała z stopwords.words()!!!
    tokens_stop = [token for token in tokens_without if token not in stop_words]
    # print(tokens)
    #Usuwa znaki specjalne, interpunkcje itd
    # tokens_without = [token for token in tokens if token.isalpha()]
    # print(tokens_without)
    # stop_words = set(stopwords.words('english')) #nazwa nie może być stopwords, żeby się nie pokrywała z stopwords.words()!!!
    # tokens_stop = [token for token in tokens_without if token not in stop_words]
    # lemmatyzacja = WordNetLemmatizer()
    # tokens_final = [lemmatyzacja.lemmatize(token) for token in tokens_stop]
    # return tokens_final, tokens_without, tokens_stop, tokens
    return tokens_lemma, tokens_without, tokens_stop, tokens


def sentiment_analysis(tekst):
    sentiment_tool = SentimentIntensityAnalyzer()
    score = sentiment_tool.polarity_scores(tekst)
    sentiment_score = score['compound']
    if sentiment_score >= 0.5:
        sentiment = 'Positive sentiment'
    elif sentiment_score <= -0.5:
        sentiment = 'Negative sentiment'
    else:
        sentiment = 'Neutral sentiment'
    return sentiment, sentiment_score, score

with open('tekst.txt', 'r') as tekst_a:
    tekst = tekst_a.read()

# tokens = processing(tekst)
# tokens, tokens_without, tokens_stop, tokens_final = processing(tekst)
tokens, tokens_without, tokens_stop, tokens_lemma = processing(tekst)
output_text = ' '.join(tokens_stop)

sentiment, sentiment_score, score = sentiment_analysis(output_text)
sentyment = str(sentiment)
wynik = str(sentiment_score)

# Analiza po zdaniach
sentiment_tool = SentimentIntensityAnalyzer()
positive_score = 0
negative_score = 0
neutral_score = 0
total_sentiment_score = 0
sentences = sent_tokenize(tekst)
sentiment_results = []
for sentence in sentences:
    scores = sentiment_tool.polarity_scores(sentence)
    sentiment_score = scores['compound']
    total_sentiment_score += sentiment_score
    if sentiment_score >= 0.5:
        sentiment = 'Positive'
        positive_score += 1
    elif sentiment_score <= -0.5:
        sentiment = 'Negative'
        negative_score += 1
    else:
        sentiment = 'Neutral'
        neutral_score += 1
    sentiment_results.append((sentence, sentiment, sentiment_score))
if positive_score > negative_score:
    overall_sentiment = 'Positive'
elif negative_score > positive_score:
    overall_sentiment = 'Negative'
else:
    overall_sentiment = 'Neutral'
average_sentiment_score = total_sentiment_score / len(sentences)

# Zapisanie wyników do nowego pliku
with open('results.txt', 'w') as nowy:
    # Analiza dla tekstu po przetworzeniu
    nowy.write('Sentiment:' + sentyment + "\n" + '\n')
    nowy.write('Sentiment score:' + wynik + "\n" + '\n')

# Plik z przetworzonym tekstem
with open('processed.txt', 'w') as nowy:
    # Analiza dla tekstu po przetworzeniu
    nowy.write("Tokens: " + str(tokens) + "\n" + '\n')
    nowy.write("Tokens, lemmatization: " + str(tokens_lemma) + "\n" + '\n')
    nowy.write("Tokens, no interpunction: " + str(tokens_without) + "\n" + '\n')
    nowy.write("Tokens, no stopwords: " + str(tokens_stop) + "\n" + '\n')
    nowy.write("Processed text:" + '\n' + str(output_text) + "\n" + '\n')

# Analiza dla zdań
with open('sentences_results.txt', 'w') as nowy:
    nowy.write("Overall:" + str(overall_sentiment) + "\n" + '\n')
    nowy.write("Overall:" + str(total_sentiment_score) + "\n" + '\n')
    nowy.write("Average:" + str(average_sentiment_score) + "\n" + '\n')
    for result in sentiment_results:
        nowy.write(f"Sentence: {result[0]}\n")
        nowy.write(f"Sentiment: {result[1]}\n")
        nowy.write(f"Sentiment Score: {result[2]}\n")
        nowy.write('\n')