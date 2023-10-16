llist=[]
with open("books.csv", "r", encoding="cp1251", errors="ignore") as file:
     for i in range(21):
          list.append(file.readline())
count=0
with open("списоккниг.txt","a") as listbook:
     for book in list:
        information=[]
        information=book.split(";")
        d='#'+str(count)+".  "+ information[3]+". "+information[1]+" - "+information[6]+"\n"
        count+=1    # count+=1 после вывода потому что я хочу выводить строка "Автор. Название - Дата поступления" и считать номером 0 
        '''information[3]= автор
           information[1]= название
           information[6]= дата постуления'''
        listbook.write(d)

