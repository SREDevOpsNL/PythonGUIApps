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
root.minsize(1652, 326)

# Create a Frame for the Entry widgets
entry_frame = tkinter.Frame(root)
button: tkinter.Button = None

# Function to handle Enter key press
def on_enter(event):
    button.invoke()

# Create a new Frame for labels and entries
label_entry_frame = tkinter.Frame(root)
#label_entry_frame.pack(fill='both', expand=True)
label_entry_frame.pack(fill='x')

# Configure the grid to expand
#label_entry_frame.grid_columnconfigure(0, weight=1)
#label_entry_frame.grid_rowconfigure(0, weight=1)

# Configure the grid to expand
for i in range(len(df.columns)):
    label_entry_frame.grid_columnconfigure(i, weight=1)
label_entry_frame.grid_rowconfigure(0, weight=1)
label_entry_frame.grid_rowconfigure(1, weight=1)

# Create a Label widget for each column
for index, column in enumerate(df.columns):
    label = tkinter.Label(label_entry_frame, text=column)
    label.grid(row=0, column=index, sticky="ew") # Grid manager to put the label in the first row. Use 'ew' to expand horizontally

# Create an Entry widget for each column
entries = {}
for index, column in enumerate(df.columns): # Loop through each column
    entry = tkinter.Entry(label_entry_frame) # Create an Entry widget
    entry.grid(row=1, column=index, sticky="ew") # Grid manager to put the entry in the second row. Use 'ew' to expand horizontally
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
button = tkinter.Button(label_entry_frame, text='Filter', command=filter_table) # Create a Button widget in the label_entry_frame
button.grid(row=1, column=len(df.columns), sticky="ew") # Add 'Filter' button to label_entry_frame, to the right of the last entry. Use 'ew' to expand horizontally

# Create a Frame for the table
table_frame = tkinter.Frame(root)
table_frame.pack(fill='both', expand=True) # Pack manager to put the frame at the bottom of the root window

# Use pandastable to create a table
pt = pandastable.Table(table_frame, dataframe=df, showtoolbar=False, showstatusbar=False)

# Function to resize the columns via ratio
def resize_columns():
    width = pt.winfo_width()
    height = pt.winfo_height()
    num_columns = len(pt.model.df.columns)
    if width > num_columns:
        # Define the ratio for each column
        column_ratios = {'title': 1.5, 'author': 0.5, 'synopsis': 2.7, 'publisher': 0.6, 'publish_date': 0.4,'page_count': 0.4, 'tags': 0.85}
        for col in pt.model.df.columns:
            ratio = column_ratios.get(col, 1)
            pt.columnwidths[col] = int(width * ratio // num_columns)
        pt.height = height  # Set the height of the table


# Bind the function to the <Configure> event of the root window
root.bind('<Configure>', lambda _: resize_columns())

# Show the table in the table_frame 
pt.show()

# Run the tkinter main loop
root.mainloop()
