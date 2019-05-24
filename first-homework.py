times=0
with open('log_files/201811113029.log',encoding='UTF-8')as f:
    for line in f:
        list1=line.split(",")[1]
        list1=list1.split(" ")[1]
        if list1=='学号：201811113029':
             times+=1
print(times)
   