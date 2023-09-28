a=0
with open("books.csv", "r", encoding="cp1251", errors="ignore") as file:
    for line in file:
        b=[]
        b=line.split(";")
        if len(b)>1:
           if len(b[1])>30:
               a+=1
print ("количество записей, у которых в поле Название строка длиннее 30 символов: ",a)