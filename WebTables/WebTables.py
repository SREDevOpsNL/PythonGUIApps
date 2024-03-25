from flask import Flask, render_template, request
from BookHierarchy import Book, BookList
import book_data
import pandas as pd

WebTables = Flask(__name__)

@WebTables.route('/', methods=['GET'])
def home():

    # Add all the books to the BookList
    book_data.add_books_to_BookList()

    # Create a DataFrame from the BookList
    books_df = pd.DataFrame([book.__dict__ for book in BookList.books])

    # Pass the list of books to the template
    return render_template('index.html', table=books_df.to_html(), columns=books_df.columns.values)

if __name__ == '__main__':
    WebTables.run(debug=True, host='0.0.0.0')