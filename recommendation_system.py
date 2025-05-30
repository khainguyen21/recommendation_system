import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
data = pd.read_csv("movies.csv", delimiter="\t" ,encoding='latin-1')

user_input = "Carrington (1995)"
top_k = 20

data['genres'] = data['genres'].apply(lambda x: x.replace("|", " ").replace("-", ""))
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data['genres'])

print(tfidf_matrix.shape)
print(vectorizer.vocabulary_)
#print(len(vectorizer.vocabulary_))

cosine_matrix = cosine_similarity(tfidf_matrix)
cosine_similarity_df = pd.DataFrame(cosine_matrix, index=data['title'], columns=data['title'])

results = cosine_similarity_df[user_input].sort_values(ascending=False)[:top_k]

my_series = pd.Series(results, name="title")

title = my_series.index
print("The most similar type of movie that we can recommend for user: ", title[0])