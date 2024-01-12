import sqlite3

db = sqlite3.connect("data.db")
cursor = db.cursor()

book_list = [
    {
        "title": "The Great Gatsby",
        "genre": "Fiction",
        "author": "F. Scott Fitzgerald",
        "description": "A timeless exploration of the American Dream set against the glittering backdrop of the Roaring Twenties.",
    },
    {
        "title": "To Kill a Mockingbird",
        "genre": "Fiction",
        "author": "Harper Lee",
        "description": "A poignant tale that confronts racial injustice in the American South, seen through the eyes of a young girl named Scout.",
    },
    {
        "title": "1984",
        "genre": "Dystopian Fiction",
        "author": "George Orwell",
        "description": "A chilling vision of a totalitarian future, where the omnipresent Big Brother surveils every aspect of society.",
    },
    {
        "title": "Pride and Prejudice",
        "genre": "Romance",
        "author": "Jane Austen",
        "description": "A classic romantic novel that explores societal expectations, love, and personal growth.",
    },
    {
        "title": "The Catcher in the Rye",
        "genre": "Fiction",
        "author": "J.D. Salinger",
        "description": "The iconic coming-of-age story of Holden Caulfield, capturing the essence of teenage angst and disillusionment.",
    },
    {
        "title": "The Hobbit",
        "genre": "Fantasy",
        "author": "J.R.R. Tolkien",
        "description": "An enchanting journey through Middle-earth as Bilbo Baggins sets out on an epic quest.",
    },
    {
        "title": "The Da Vinci Code",
        "genre": "Mystery",
        "author": "Dan Brown",
        "description": "A gripping modern mystery that intertwines art, history, and religion in a labyrinth of secrets.",
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "genre": "Fantasy",
        "author": "J.K. Rowling",
        "description": "The magical initiation into the wizarding world, following the adventures of the young wizard Harry Potter.",
    },
    {
        "title": "The Hunger Games",
        "genre": "Dystopian Fiction",
        "author": "Suzanne Collins",
        "description": "A riveting dystopian saga where Katniss Everdeen becomes the reluctant symbol of rebellion.",
    },
    {
        "title": "The Alchemist",
        "genre": "Philosophical Fiction",
        "author": "Paulo Coelho",
        "description": "A philosophical journey of self-discovery and destiny as a shepherd named Santiago pursues his dreams.",
    },
    {
        "title": "Brave New World",
        "genre": "Dystopian Fiction",
        "author": "Aldous Huxley",
        "description": "An exploration of a utopian society where conformity and happiness are carefully engineered.",
    },
    {
        "title": "The Lord of the Rings",
        "genre": "Fantasy",
        "author": "J.R.R. Tolkien",
        "description": "A monumental epic of Middle-earth, chronicling the quest to destroy the One Ring and save the world.",
    },
    {
        "title": "Crime and Punishment",
        "genre": "Fiction",
        "author": "Fyodor Dostoevsky",
        "description": "A psychological thriller delving into the moral consequences of a young man's actions.",
    },
    {
        "title": "The Shining",
        "genre": "Horror",
        "author": "Stephen King",
        "description": "A spine-chilling tale of supernatural horror as a family confronts the malevolent forces within an isolated hotel.",
    },
    {
        "title": "The Picture of Dorian Gray",
        "genre": "Gothic Fiction",
        "author": "Oscar Wilde",
        "description": "A haunting exploration of the consequences of hedonism and the pursuit of eternal youth.",
    },
    {
        "title": "One Hundred Years of Solitude",
        "genre": "Magical Realism",
        "author": "Gabriel Garcia Marquez",
        "description": "A multi-generational saga blending magical elements with the history of a fictional town.",
    },
    {
        "title": "The Road",
        "genre": "Post-Apocalyptic Fiction",
        "author": "Cormac McCarthy",
        "description": "A harrowing journey through a post-apocalyptic landscape as a father and son seek survival.",
    },
    {
        "title": "Moby-Dick",
        "genre": "Adventure",
        "author": "Herman Melville",
        "description": "A monumental tale of obsession and revenge on the high seas, featuring the enigmatic Captain Ahab.",
    },
    {
        "title": "The Kite Runner",
        "genre": "Historical Fiction",
        "author": "Khaled Hosseini",
        "description": "A poignant exploration of friendship, betrayal, and redemption set against the backdrop of Afghanistan.",
    },
    {
        "title": "The Girl with the Dragon Tattoo",
        "genre": "Mystery",
        "author": "Stieg Larsson",
        "description": "A gripping mystery featuring investigative journalist Mikael Blomkvist and the enigmatic hacker Lisbeth Salander.",
    },
]

cursor.execute('''
    CREATE TABLE IF NOT EXISTS register (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first TEXT NOT NULL,
        last TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')


# cursor.execute(f"DROP TABLE register")
# person = cursor.fetchall()

cursor.execute(f"SELECT * FROM register WHERE email='vawate2003@gmail.com'")
person = cursor.fetchall()
cursor.execute(f"SELECT * FROM preferences WHERE id='{person[0][0]}'")
preferences = cursor.fetchall()
cursor.execute(f"SELECT * FROM books WHERE genre='{preferences[0][1]}' OR author='{preferences[0][2]}'")
output = cursor.fetchall()
print(output[1][1])
# for book in book_list:
#     cursor.execute('''
#         INSERT INTO books (title, author, genre, description)
#         VALUES (?, ?, ?, ?)
#     ''', (book['title'], book['author'], book['genre'], book['description']))
#     db.commit()

# cursor.execute("SELECT * FROM books WHERE genre=?", ("Fiction",))
# recommendations = cursor.fetchall()

# # Extract titles from the recommendations list
# book_titles = [recommendation[1] for recommendation in recommendations]

# # Now you can use the book_titles array as needed
# print(book_titles)

# cursor = db.cursor()
# cursor.execute("SELECT * FROM books where id=1")
# books = cursor.fetchall()
# book = [] 
# for b in books:
#     temp = [b[0],b[1],b[2],b[3],b[4]]
#     book.append(temp)
    
# print(book[0][2])
# genre = f"{book[0][2]}"
# cursor.execute(f"SELECT * FROM books WHERE genre='{book[0][2]}'")
# recommendations = cursor.fetchall()

# db.commit()
# books = []
# for recommendation in recommendations:
#     temp = [recommendation[0],recommendation[1],recommendation[2],recommendation[3],recommendation[4]]
#     books.append(temp)

# book_titles = [recommendation[1] for recommendation in recommendations]
# print(books)
# print(book_titles)



# Commit the changes and close the connection
db.commit()
db.close()