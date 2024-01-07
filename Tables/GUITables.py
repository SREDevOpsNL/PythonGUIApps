import pandas
import tkinter
from tkinter import ttk
import pandastable
from BookHierarchy import Book, BookList
import book_data  #Add all the books to the BookList

# Add all the books to the BookList
book_data.add_books_to_BookList()

# Create a DataFrame from the BookList
list = [book.__dict__ for book in BookList.books]
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
