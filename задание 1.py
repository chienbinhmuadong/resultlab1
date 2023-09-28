a=0
with open("books.csv", "r", encoding="cp1251", errors="ignore") as file:
     for line in file:
          if len(line)>2:
            a+=1
print("количество записей в файле: ",a)