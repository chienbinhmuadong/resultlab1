list=[]
with open("books.csv", "r", encoding="cp1251", errors="ignore") as file:
     for i in range(21):
          list.append(file.readline())
a=0

with open("списоккниг.txt","a") as listbook:
     for i in range(1,len(list)):
        b=[]
        b=list[i].split(";")
        d='#'+str(i)+".  "+ b[3]+". "+b[1]+" - "+b[6]+"\n"
        listbook.write(d)


