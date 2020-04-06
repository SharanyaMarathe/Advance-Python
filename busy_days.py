booked=[1,3,9,12,13,18,26,27,28,29]
travel=[4,5,15,16,21,22]
month=list(range(1,31))
free_list=list()
busy=booked+travel
free_list=[item for item in month if item not in busy]
print(free_list)
'''for i in travel:
    booked.append(i)
for item in month:
    if item not in booked:
        free_list.append(item)
        
print(free_list)'''
