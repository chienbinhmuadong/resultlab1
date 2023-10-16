MAX_NAME_LIM = 30
book_count=0
with open("books.csv", "r", encoding="cp1251", errors="ignore") as file:
    for line in file:
        book_entry=[]
        book_entry=line.split(";")
        book_name = book_entry[1]
        if len(book_name)>MAX_NAME_LIM:
              book_count+=1
print (f"количество записей, у которых в поле Название строка длиннее 30 символов: {book_count}")
