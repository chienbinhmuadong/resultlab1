books_count=0
with open("books.csv", "r", encoding="cp1251", errors="ignore") as file:
     for line in file:
          books_count+=1
print(f"количество записей в файле: {books_count}")
