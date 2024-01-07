import pandas
import tkinter
from tkinter import ttk
import pandastable
import BookHierarchy as bh


Hobbit = {
    'title': 'The Hobbit',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Synopsis',
    'publisher': 'George Allen & Unwin',
    'publish_date': '1937-09-21',
    'page_count': 310,
    'tags': ['Fantasy', 'Adventure']
}
the1stBook = bh.Book(**Hobbit)

timedelta_to_read = the1stBook.get_reading_time()
time_hours = timedelta_to_read.seconds//3600
time_minutes = (timedelta_to_read.seconds//60)%60
time_str = f"{time_hours} hours and {time_minutes} minutes"
age = int(abs(the1stBook.get_published_age().days) / 365.25)

StringTimeToReadHobbit = f"It takes {time_str} to read {the1stBook},\nwhich was published {age} years ago."

if bh.BookList.books is None:
    bh.BookList.books = []

bh.BookList.add(the1stBook)

Fellowship = {
    'title': 'The Fellowship of the Ring',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Synopsis',
    'publisher': 'George Allen & Unwin',
    'publish_date': '1954-07-29',
    'page_count': 423,
    'tags': ['Fantasy', 'Adventure']
}
bh.BookList.add(bh.Book(**Fellowship))

TwoTowers = {
    'title': 'The Two Towers',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Synopsis',
    'publisher': 'George Allen & Unwin',
    'publish_date': '1954-11-11',
    'page_count': 352,
    'tags': ['Fantasy', 'Adventure']
}
bh.BookList.add(bh.Book(**TwoTowers))

ReturnOfTheKing = {
    'title': 'The Return of the King',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Synopsis',
    'publisher': 'George Allen & Unwin',
    'publish_date': '1955-10-20',
    'page_count': 416,
    'tags': ['Fantasy', 'Adventure']
}
bh.BookList.add(bh.Book(**ReturnOfTheKing))

magicDate = '1950-01-01'

list = [book.__dict__ for book in bh.BookList.books]
typeOfVar = type(list)
df = pandas.DataFrame(list)

# Create a root window and immediately hide it
root = tkinter.Tk()

# # Create a Frame
# frame = tkinter.Frame(root)
# frame.pack(fill='both', expand=True)

# # Use pandastable to create a table
# pt = pandastable.Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)
# #pt.enable_sorting()
# pt.show()

# Create a Frame for the Entry widgets
entry_frame = tkinter.Frame(root)
entry_frame.pack(fill='x')

button: tkinter.Button = None

# Function to handle Enter key press
def on_enter(event):
    button.invoke()

# Create an Entry widget for each column
entries = {}
for column in df.columns:
    label = tkinter.Label(entry_frame, text=column)
    label.pack(side='left')
    entry = tkinter.Entry(entry_frame)
    entry.pack(side='left')
    entries[column] = entry
    entry.bind('<Return>', on_enter)

# Function to filter the DataFrame and update the table
def filter_table():
    filtered_df = df.copy()
    for column, entry in entries.items():
        value = entry.get()
        if value:
            filtered_df = filtered_df[filtered_df[column].astype(str).str.contains(value)]
    pt.updateModel(pandastable.TableModel(filtered_df))
    pt.redraw()

# Button to apply the filters
button = tkinter.Button(root, text='Filter', command=filter_table)
button.pack()

# Create a Frame for the table
table_frame = tkinter.Frame(root)
table_frame.pack(fill='both', expand=True)

# Use pandastable to create a table
pt = pandastable.Table(table_frame, dataframe=df, showtoolbar=True, showstatusbar=True)
pt.show()

# Run the tkinter main loop
root.mainloop()

# "The Silmarillion" (1977) - This book contains Tolkien's mythopoeic tales, providing extensive background and history to the world of Middle-earth.

# "Unfinished Tales of Númenor and Middle-earth" (1980) - A collection of narratives and stories that were incomplete or unpublished during Tolkien's lifetime, offering further insight into Middle-earth's history.

# "The Children of Húrin" (2007) - This novel presents a complete and expanded version of one of the tales found in "The Silmarillion," focusing on the tragic story of Túrin Turambar.

# "The Fall of Gondolin" (2018) - Edited by Christopher Tolkien, this book delves into the story of the legendary city of Gondolin, showcasing its downfall.
