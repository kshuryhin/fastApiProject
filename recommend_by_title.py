import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

books = pd.read_csv('books.csv')
books['authors'] = books['authors'].fillna('')

books['combined_features'] = books['title'] + ' ' + books['authors']

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_books(title, num_recommendations=5):
    idx = books.index[books['title'] == title].tolist()[0]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:num_recommendations + 1]

    book_indices = [i[0] for i in sim_scores]

    return books[['title', 'thumbnail', 'description', 'average_rating']].iloc[book_indices]