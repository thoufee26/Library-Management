from tkinter import *
from tkinter import messagebox  

books = []  # title, author, year, code

def add_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    code = entry_code.get()

    if title and author and year and code:
        book = {"Title": title, "Author": author, "Published Year": year, "Code": code}
        books.append(book)
        update_listbox()
        clear_entries()  
        messagebox.showinfo("Success", "Book Added Successfully.")
    else:
        messagebox.showwarning("Error", "Please Fill All fields.")

def update_listbox():
    listbox.delete(0, END)  
    for book in books:
        listbox.insert(END, f"{book['Title']} by {book['Author']} in {book['Published Year']} , Code: {book['Code']}")

def clear_entries():
    entry_title.delete(0, END)
    entry_author.delete(0, END)
    entry_year.delete(0, END)
    entry_code.delete(0, END)

def delete_book():
    selected_item_index = listbox.curselection()
    if selected_item_index:
        selected_item = listbox.get(selected_item_index)
        code_to_delete = selected_item.split(" , Code: ")[1]
        # Remove the book from the list
        global books
        books = [book for book in books if book["Code"] != code_to_delete]
        update_listbox()
        messagebox.showinfo("Success", f"Book with code {code_to_delete} deleted successfully.")
    else:
        messagebox.showwarning("Selection Error", "Please select a book to delete.")

root = Tk()
root.title("Library Books Data Management")
root.geometry("700x400")

label_title = Label(root, text="Title")
label_title.place(x=40, y=40)
entry_title = Entry(root)
entry_title.place(x=150, y=40)

label_author = Label(root, text="Author")
label_author.place(x=40, y=100)
entry_author = Entry(root)
entry_author.place(x=150, y=100)

label_year = Label(root, text="Year")
label_year.place(x=40, y=160)
entry_year = Entry(root)
entry_year.place(x=150, y=160)

label_code = Label(root, text="Code")
label_code.place(x=40, y=220)
entry_code = Entry(root)
entry_code.place(x=150, y=220)

add_button = Button(root, text="Add Book", command=add_book)
add_button.place(x=180, y=260)

label_books = Label(root, text="Books Details", font="arial 20 bold")
label_books.place(x=380, y=40)  
listbox = Listbox(root, width=60, height=12)
listbox.place(x=300, y=80)

delete_button = Button(root, text="Delete Selected Book",command=delete_book)
delete_button.place(x=420, y=300)

root.mainloop()
