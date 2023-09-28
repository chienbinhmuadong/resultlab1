diction=dict({})
title=[]
with open("books.csv",'r', encoding="cp1251", errors='ignore')as file:
    l=file.readline()
    title=l.split(';')
    for line in file:
        a=[]
        a=line.split(';')
        if len(a)>=2:
            if a[3] in diction:
               diction[a[3]].append(a)
            else:
               diction[a[3]]=[]
               diction[a[3]].append(a)

name=input("поиск книги по автору: ")  
print("информация о книге:\n")

if name in diction:
        t=diction[name]
        if len(t)==1:
            for i in range(len(title)):
                print(title[i].rstrip,": ",t[i])
        else:
            print(title,':')
            for i in range(len(t)):
                print(t[i])
        

