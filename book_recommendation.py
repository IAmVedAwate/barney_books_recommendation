from dotenv import load_dotenv
# from langchain.embeddings import FakeEmbeddings
from langchain_community.embeddings import FakeEmbeddings
import numpy as np
import faiss
import sqlite3

class BookRecommendation:
    def __init__(self, book_titles):
        self.fake_embeddings = FakeEmbeddings(size=1536)
        self.book_titles = book_titles
        self.fake_embeddings_list = self._embed_titles()

        # Build the Faiss index
        self.index = faiss.IndexFlatL2(1536)
        self.index.add(self.fake_embeddings_list)

    def _embed_titles(self):
        embeddings_list = []
        for title in self.book_titles:
            embeddings_list.append(self.fake_embeddings.embed_query(title))
        return np.array(embeddings_list).astype("float32")

    def recommend_books_by_count(self, query_title, count):
        k = count
        query_embedding = np.array([self.fake_embeddings.embed_query(query_title)]).astype("float32")
        distances, indices = self.index.search(query_embedding, k)
        return np.array(self.book_titles)[indices].tolist()

    def recommend_books(self, query_title):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # Execute the SQL query to get the count of books
        cursor.execute('SELECT COUNT(*) FROM books')  # Assuming 'books' is the name of your table

        # Fetch the result
        book_count = cursor.fetchone()[0]
        k=int(book_count)

        # Close the database connection
        connection.close()
        query_embedding = np.array([self.fake_embeddings.embed_query(query_title)]).astype("float32")
        distances, indices = self.index.search(query_embedding, k)
        return np.array(self.book_titles)[indices].tolist()
    
if __name__ == "__main__":
    load_dotenv(".env")
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    # Example usage
    cursor.execute("SELECT * FROM books")
    recommendations = cursor.fetchall()

    # Extract titles from the recommendations list
    book_titles = [recommendation[1] for recommendation in recommendations]

    book_recommendation = BookRecommendation(book_titles)

    # Example: Recommend books based on a query title
    query_title = "Game Of Thrones"
    recommended_books = book_recommendation.recommend_books(query_title)
    print(recommended_books)
