# GUITables.py

This Python script uses the `pandas`, `tkinter`, and `pandastable` libraries to create a graphical user interface (GUI) that displays a table of books. The table can be filtered based on user input.

The script begins by importing the necessary libraries and modules. `pandas` is used for data manipulation, `tkinter` and `ttk` for creating the GUI, and `pandastable` for displaying the data in a table format. It also imports `Book` and `BookList` classes from `BookHierarchy` module and `book_data` module which is used to add books to the `BookList`.

The script adds books to the `BookList` using the `add_books_to_BookList` function from `book_data` module. It then creates a pandas DataFrame from the `BookList`. Each book in the `BookList` is an instance of the `Book` class, and `book.__dict__` is used to convert each `Book` object into a dictionary.

A root window is created using `tkinter.Tk()`. The minimum size of the window is set using the `minsize` method.

A new frame is created to hold the labels and entries for each column in the DataFrame. The grid is configured to expand as needed. For each column in the DataFrame, a label and an entry widget are created. The labels are placed in the first row of the grid, and the entry widgets in the second row. The entry widgets are stored in a dictionary, `entries`, with the column names as keys.

The `filter_table` function is used to filter the DataFrame based on the user's input in the entry widgets. For each entry, if a value is present, the DataFrame is filtered to only include rows where the corresponding column contains that value. The table is then updated with the filtered DataFrame.

Finally, a button is created to apply the filters. When clicked, it calls the `filter_table` function.
