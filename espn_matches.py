def mtches_sorted():
        
        for line in file:
            info=line.split(",")
            print(info)
            match_player[info[0]]=info[2]



match_player={}
with open ("captains.txt",mode='r') as file:
                 header=next(file)
                 mtches_sorted()
sorted(match_player,key=ms())
print(match_player)
