import csv, operator

dic = {}

with open('football.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(spamreader, None)  
    for row in spamreader:
        dic[row[0]] = int(row[5]) - int(row[6])

print("Listado menor")
sorted_x = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for item in sorted_x:
    print(item[0] + ' con menor diferencia de ' + str(item[1]))
    
print("Listado mayor")
sorted_x = sorted(dic.items(), key=lambda x: x[1])

for item in sorted_x:
    print(item[0] + ' con mayor diferencia de ' + str(item[1]))
