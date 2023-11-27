import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

books = pd.read_csv('books.csv')
books['description'] = books['description'].fillna('')
books['authors'] = books['authors'].fillna('')
books['categories'] = books['categories'].fillna('')

books['combined_features'] = books['title'] + ' ' + books['authors'] + ' ' + books['description'] + ' ' + books['categories']

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


def recommend_books_based_on_description(description, num_recommendations=5):
    description_tfidf = tfidf.transform([description])

    sim_scores = cosine_similarity(description_tfidf, tfidf_matrix).flatten()

    top_indices = sim_scores.argsort()[-num_recommendations:][::-1]

    return books[['title', 'thumbnail', 'description', 'average_rating']].iloc[top_indices]