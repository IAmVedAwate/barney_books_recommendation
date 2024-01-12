from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import sqlite3
from book_recommendation import BookRecommendation

app = Flask(__name__)

# book_recommendation = BookRecommendation(book_titles)

app.secret_key = 'your_secret_key'

def get_conn():
    db = sqlite3.connect("data.db")
    return db

@app.route('/')
def home():
    email = session.get('email')

    if not email:
        return redirect("login")

    return redirect("all_books")


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/all_books')
def all_books():
    
    email = session.get('email')

    if not email:
        return redirect("login")

    db = get_conn()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    recommendations = cursor.fetchall()


    books = []
    for recommendation in recommendations:
        temp = [recommendation[0],recommendation[1],recommendation[2],recommendation[3],recommendation[4]]
        books.append(temp)

    book_titles = [recommendation[1] for recommendation in recommendations]
    book_recommendation = BookRecommendation(book_titles)
    cursor.execute(f"SELECT * FROM register WHERE email='{email}'")
    person = cursor.fetchall()
    cursor.execute(f"SELECT * FROM preferences WHERE id='{person[0][0]}'")
    preferences = cursor.fetchall()
    cursor.execute(f"SELECT * FROM books WHERE genre='{preferences[0][1]}' OR author='{preferences[0][2]}'")
    output = cursor.fetchall()
    titles_array = book_recommendation.recommend_books(f"{output[0][1]}")
    entries = []
    for title in titles_array[0]:
        for book in books:
            if book[1] == title:
                entries.append(book)
    db.commit()
    db.close()
    return render_template("all_books.html",entries=entries)


@app.route("/login_submit",methods=['POST'])
def login_submit():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_conn()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM register")
        entries = cursor.fetchall()
        db.commit()
        db.close()
        for i in range(len(entries)):
            if email == f"{entries[i][3]}" and password== f"{entries[i][4]}":
                session['email'] = f"{entries[i][3]}"
                return redirect(url_for('all_books'))
        else:
            msg="Login Invalid"
            return render_template('login.html', msg=msg)

@app.route('/register_submit', methods=['POST'])
def register_submit():

    if request.method == 'POST':
        first = request.form['first']
        last = request.form['last']
        password = request.form['password']
        genre = request.form['genre']
        author = request.form['author']
        email = request.form['email']
        con_pass = request.form['con_password']
        
        if password != con_pass:
            msg="Password Confirmation Failed"
            return render_template('register.html', msg=msg)
        session['email'] = email  
        
        db = get_conn()
        cursor = db.cursor()
        q = '''
            INSERT INTO register (first, last, email, password)
            VALUES (?, ?, ?, ?)
        '''
        q2 = '''
            INSERT INTO preferences (genre, author)
            VALUES (?, ?)
        '''
        cursor.execute(q,(first, last, email, password))
        db.commit()
        cursor.execute(q2,(genre, author))
        db.commit()
        db.close()  

    return redirect(url_for('all_books'))


@app.route('/book', methods=['GET','POST'])
def book():
    book_id = request.args.get('id')
    if book_id:
        email = session.get('email')

        if not email:
            return redirect("/login")
        
        db = get_conn()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM books where id={book_id}")
        book_by_id = cursor.fetchall()
        book = [] 
        for b in book_by_id:
            temp = [b[0],b[1],b[2],b[3],b[4]]
            book.append(temp)
            
        cursor.execute(f"SELECT * FROM books WHERE genre='{book[0][2]}'")
        recommendations = cursor.fetchall()
        
        db.commit()
        db.close()
        
        books = []
        for recommendation in recommendations:
            temp = [recommendation[0],recommendation[1],recommendation[2],recommendation[3],recommendation[4]]
            books.append(temp)
        book_count = len(books)
        book_titles = [recommendation[1] for recommendation in recommendations]
        book_recommendation = BookRecommendation(book_titles)
        titles_array = book_recommendation.recommend_books_by_count(book[0][1],book_count)
        entries = []
        for title in titles_array[0]:
            for b2 in books:
                if b2[1] == title:
                    entries.append(b2)
        book_titles = [recommendation[1] for recommendation in recommendations]
        book_recommendation = BookRecommendation(book_titles)
        

        return render_template("book.html",book=book,entries=entries)
    else:
        return redirect("all_books")

@app.route('/logout')
def logout():
    session['email'] = None
    return redirect("login")



if __name__ == '__main__':
    app.run(debug=True)
