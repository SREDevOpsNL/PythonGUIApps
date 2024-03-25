# GUITables.py Desktop Application

This Python script uses the `pandas`, `tkinter`, and `pandastable` libraries to create a graphical user interface (GUI) that displays a table of books. The table can be filtered based on user input.

The script begins by importing the necessary libraries and modules. `pandas` is used for data manipulation, `tkinter` and `ttk` for creating the GUI, and `pandastable` for displaying the data in a table format. It also imports `Book` and `BookList` classes from `BookHierarchy` module and `book_data` module which is used to add books to the `BookList`.

The script adds books to the `BookList` using the `add_books_to_BookList` function from `book_data` module. It then creates a pandas DataFrame from the `BookList`. Each book in the `BookList` is an instance of the `Book` class, and `book.__dict__` is used to convert each `Book` object into a dictionary.

A root window is created using `tkinter.Tk()`. The minimum size of the window is set using the `minsize` method.

A new frame is created to hold the labels and entries for each column in the DataFrame. The grid is configured to expand as needed. For each column in the DataFrame, a label and an entry widget are created. The labels are placed in the first row of the grid, and the entry widgets in the second row. The entry widgets are stored in a dictionary, `entries`, with the column names as keys.

The `filter_table` function is used to filter the DataFrame based on the user's input in the entry widgets. For each entry, if a value is present, the DataFrame is filtered to only include rows where the corresponding column contains that value. The table is then updated with the filtered DataFrame.

Finally, a button is created to apply the filters. When clicked, it calls the `filter_table` function.

# WebTables Web Application

This application is a Flask web application that displays a list of books. The books are defined in the `BookHierarchy.py` and `book_data.py` files and displayed using the `WebTables.py` file.

## WebTables.py
This is the main file of the Flask application. It defines a single route, the home route (`/`), which can handle `GET` requests.

When a request is made to the home route, the `add_books_to_BookList` function is called to add all the books to the `BookList`. `books_df` DataFrame is created from a list of Book objects. Each Book object is converted to a dictionary using book.__dict__, and these dictionaries are used to create the DataFrame. This is done using a list comprehension.

Finally, the list of books is passed to the `index.html` template using the `render_template` function. This template is responsible for displaying the list of books on the web page.

WebTables starts by importing the necessary modules:

```
from flask import Flask, render_template, request from BookHierarchy import Book, BookList import book_data import pandas as pd
```

Then, it initializes a Flask application:

```
WebTables = Flask(__name__)
```

The application defines a single route, the home route (/), which can handle GET requests:

```
@WebTables.route('/', methods=['GET']) def home():
```

When a request is made to the home route, the add_books_to_BookList function from book_data module is called to add all the books to the BookList:

book_data.add_books_to_BookList()

Next, a pandas DataFrame books_df is created from the BookList. Each Book object in the BookList is converted to a dictionary using book.__dict__, and these dictionaries are used to create the DataFrame. This is done using a list comprehension:

```
books_df = pd.DataFrame([book.__dict__ for book in BookList.books])
```

Finally, the DataFrame is passed to the index.html template using the render_template function:

```
return render_template('index.html', table=books_df.to_html(), columns=books_df.columns.values)
```

This template is responsible for displaying the list of books on the web page.

## BookHierarchy.py

This file defines the `Book` and `BookList` classes. The `Book` class represents a single book, with properties such as title, author, and reading time. The `BookList` class is a collection of `Book` objects.

### Book Class
The Book class represents a single book, with properties such as title, author, and reading time. The BookList class is a collection of Book objects. The Book class is defined in BookHierarchy.py. It has several properties, including title, author, and reading_time. Each Book object represents a single book.

### BookList Class
The BookList class is also defined in BookHierarchy.py. It has a static property books that holds a list of Book objects. The add_books_to_BookList function from book_data module is used to add books to this list.

## book_data.py

This file is responsible for adding books to the `BookList`. It defines a function `add_books_to_BookList` that creates new `Book` objects and adds them to the `BookList`.