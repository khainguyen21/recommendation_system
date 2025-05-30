🎬 Movie Genre Recommender Using TF-IDF & Cosine Similarity
This is a simple content-based movie recommender system built with Python, using TF-IDF vectorization and cosine similarity to find and suggest movies with similar genres.

📌 Project Overview
This project demonstrates a basic approach to recommending movies based on their genres. Given a movie title as input, the system finds the most similar movies in terms of genre by analyzing a dataset using the following techniques:

Text preprocessing of genres

TF-IDF vectorization of genre descriptions

Cosine similarity to measure closeness between movies

🛠 Technologies Used
Python

Pandas

scikit-learn (TF-IDF, Cosine Similarity)

📂 Dataset
The dataset should be a tab-delimited file (.csv) with at least the following columns:

title: the movie title

genres: genre tags separated by | (e.g., Drama|Romance|Biography)

Filename: movies.csv
Encoding: latin-1
Delimiter: \t

⚠️ Make sure the dataset is in the same directory as the script.

🚀 How It Works
Genres are preprocessed by replacing | and - with spaces.

The genre strings are transformed into TF-IDF vectors.

Cosine similarity is computed between all movie pairs.

Based on a user's movie input, the top-k most similar movies (by genre) are recommended.

🔍 Sample Usage
python
Copy
Edit
user_input = "Carrington (1995)"
top_k = 20
Example output:

pgsql
Copy
Edit
The most similar type of movie that we can recommend for user:  Carrington (1995)
📈 Output
The system prints:

Shape of the TF-IDF matrix

TF-IDF vocabulary (word index)

Top k similar movie titles based on genre similarity

🧠 Future Improvements
Add support for fuzzy matching of titles

Include metadata like plot summaries or tags for richer similarity

Build a web app or GUI interface

Use a larger and more diverse dataset

📝 License
This project is open source and available under the MIT License.
