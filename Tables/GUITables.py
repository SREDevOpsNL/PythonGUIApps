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

Silmarillion = {
    'title': 'The Silmarillion',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Collection of mythopoeic tales providing extensive background to Middle-earth.',
    'publisher': 'George Allen & Unwin',
    'publish_date': '1977-10-20',
    'page_count': 365,
    'tags': ['Fantasy', 'Mythopoeia']
}
bh.BookList.add(bh.Book(**Silmarillion))

UnfinishedTales = {
    'title': 'Unfinished Tales of Númenor and Middle-earth',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Collection of narratives and incomplete stories providing further insight into Middle-earth.',
    'publisher': 'George Allen & Unwin',
    'publish_date': '1980-10-21',
    'page_count': 472,
    'tags': ['Fantasy', 'Narratives']
}
bh.BookList.add(bh.Book(**UnfinishedTales))

ChildrenOfHurin = {
    'title': 'The Children of Húrin',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Complete and expanded version of a tale found in "The Silmarillion," focusing on the tragic story of Túrin Turambar.',
    'publisher': 'Houghton Mifflin',
    'publish_date': '2007-11-22',
    'page_count': 320,
    'tags': ['Fantasy', 'Tragedy']
}
bh.BookList.add(bh.Book(**ChildrenOfHurin))

FallOfGondolin = {
    'title': 'The Fall of Gondolin',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Tells the story of the legendary city of Gondolin and its downfall, edited by Christopher Tolkien.',
    'publisher': 'HarperCollins',
    'publish_date': '2018-12-23',
    'page_count': 304,
    'tags': ['Fantasy', 'Legendary']
}
magicDate = '1950-01-01'
bh.BookList.add(bh.Book(**FallOfGondolin))

list = [book.__dict__ for book in bh.BookList.books]
typeOfVar = type(list)
df = pandas.DataFrame(list)

# Create a root window and immediately hide it
root = tkinter.Tk()

# Set the minimum window size
root.minsize(1212, 326)

# Create a Frame for the Entry widgets
entry_frame = tkinter.Frame(root)
entry_frame.pack(fill='x') # Pack manager to put the frame at the top of the root window

button: tkinter.Button = None

# Function to handle Enter key press
def on_enter(event):
    button.invoke()

# Create an Entry widget for each column
entries = {}
for index, column in enumerate(df.columns):
    label = tkinter.Label(entry_frame, text=column)
    label.pack(side='left') # Pack manager to put the label to the left of the entry widget
    entry = tkinter.Entry(entry_frame)
    entry.pack(side='left') # Pack manager to put the entry widget to the right of the label
    entry.pack(fill=tkinter.BOTH, expand=1)
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
button.pack() # Pack manager to put the button at the bottom of the root window

# Create a Frame for the table
table_frame = tkinter.Frame(root)
table_frame.pack(fill='both', expand=True) # Pack manager to put the frame at the bottom of the root window

# Use pandastable to create a table
pt = pandastable.Table(table_frame, dataframe=df, showtoolbar=False, showstatusbar=False)
#pt = pandastable.Table(entry_frame, dataframe=df, showtoolbar=True, showstatusbar=True)

counter = 0

# Function to resize the columns
def resize_columns():
    width = pt.winfo_width()
    height = pt.winfo_height()
    num_columns = len(pt.model.df.columns)
    if width > num_columns:
        column_width = width // num_columns
        for col in pt.model.df.columns:
            pt.columnwidths[col] = column_width
        pt.height = height  # Set the height of the table

# Bind the function to the <Configure> event of the root window
root.bind('<Configure>', lambda _: resize_columns())

# Show the table in the table_frame 
pt.show()

# Run the tkinter main loop
root.mainloop()
