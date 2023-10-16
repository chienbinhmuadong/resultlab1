diction = {}
title=[]
with open("books.csv",'r', encoding="cp1251", errors='ignore')as file:
    title=file.readline().split(';') # title это первая строка ID, Название, Тип, Автор...
    for line in file:
        book=[]
        book=line.split(';')
        if len(book)>=2:
            name_author=book[3]
            if name_author in diction:
               diction[name_author].append(book)
            else:
               diction[name_author]=[]
               diction[name_author].append(book)

name=input("поиск книги по автору: ")  
print("информация о книге:\n")

if name in diction:
        infor_book=diction[name]
        if len(infor_book)==1:
            for i in range(len(title)):
                print(f"{title[i].rstrip} : {infor_book[i]}")
        else:
            print(title,':')
            for i in range(len(infor_book)):
                print(infor_book[i])
