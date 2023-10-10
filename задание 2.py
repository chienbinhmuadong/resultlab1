book_counts=0
with open("books.csv", "r", encoding="cp1251", errors="ignore") as file:
    for line in file:
        book=[]
        book=line.split(";")
        if len(book)>1:
           if len(book[1])>30:
               book_counts+=1
print ("количество записей, у которых в поле Название строка длиннее 30 символов: ",a)
