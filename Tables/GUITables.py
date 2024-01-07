import pandas
import tkinter
from tkinter import ttk
import pandastable
from BookHierarchy import Book, BookList
import book_data  #Add all the books to the BookList

# Add all the books to the BookList
book_data.add_books_to_BookList()

# Create a DataFrame from the BookList
df = pandas.DataFrame([book.__dict__ for book in BookList.books])

# Create a root window and immediately hide it
root = tkinter.Tk()

# Assign minimum width and height of the root window
min_width = 1652
min_height = 326
# Set the minimum window size
root.minsize(min_width, min_height)

# Create a button to invoke the filter function
filter_button: tkinter.Button = None

# Function to handle Enter key press
def on_enter(event):
    filter_button.invoke()

# Create a new Frame for labels and entries
label_entry_frame = tkinter.Frame(root)
#label_entry_frame.pack(fill='both', expand=True) # expand=True to fill the entire root window and fill='both' to resize horizontally and vertically
label_entry_frame.pack(fill='x') # to resize horizontally only

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
filter_button = tkinter.Button(label_entry_frame, text='Filter', command=filter_table) # Create a Button widget in the label_entry_frame
filter_button.grid(row=1, column=len(df.columns), sticky="ew") # Add 'Filter' button to label_entry_frame, to the right of the last entry. Use 'ew' to expand horizontally

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
        column_ratios = {'title': 1.5, 'author': 0.5, 'synopsis': 1.7, 'publisher': 0.6, 'publish_date': 0.4,'page_count': 0.4, 'tags': 0.85}
        for col in pt.model.df.columns:
            ratio = column_ratios.get(col, 1)
            pt.columnwidths[col] = int(width * ratio // num_columns)
        pt.height = height  # Set the height of the table


# Bind the function to the <Configure> event of the root window
root.bind('<Configure>', lambda _: resize_columns())

def show_details(event):
    # Create a new Toplevel window
    details_window = tkinter.Toplevel(root)
    # Create a Treeview widget
    tree = ttk.Treeview(details_window, columns=('col', 'value'), show='')

    # Get the indices of the selected rows
    selected_indices = pt.multiplerowlist
    # Get the selected rows from the DataFrame
    selected_df = pt.model.df.iloc[selected_indices]
    dict_of_details = [dict(row.items()) for _, row in selected_df.iterrows()][0]
    # Calculate the maximum length of the values
    max_length = max(len(str(value)) for value in dict_of_details.values())

    # multiplier to adjust the width of the Treeview based on maximum length of the values
    multiplier = 6
    # Set the width of the Treeview and window
    tree.column('value', width=max_length * multiplier)
    width = max_length * multiplier + 202
    max_height = len(dict_of_details) * 20
    # Set the size of popup window 
    details_window.minsize(width, max_height)
    details_window.maxsize(width, max_height)
    details_window.geometry(f'{width}x{max_height}')  # Adjust the size as needed
    # Display the row details in the new window
    for item in dict_of_details:
            tree.insert('', 'end', values=(item, dict_of_details[item]))
    # Adjust the height of the Treeview based on the number of items
    tree.configure(height=len(tree.get_children()))
    tree.pack()

pt.bind('<Double-1>', show_details)

# Show the table in the table_frame 
pt.show()

# Run the tkinter main loop
root.mainloop()