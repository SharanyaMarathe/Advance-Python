'''def get_matches():
        for line in file:
            info=line.split(",")
            #print(info)
            match_player[info[0]]=int(info[2])
            
        for key in sorted(match_player,key=get_val,reverse=True):
              print(key,match_player[key])'''
def match_array():
        for line in file:
            info=line.split(",")
            #print(info)
            w=info[7].split("\n")
            MatchDetails_captains[info[0]]=list(map(int,info[2:5]))
            #[int(info[2]),int(info[3]),int(info[4]),float(w[0])]

        print("Name\t\t\tMathes\t\t\tWon\t\t\tLost")    
        for key in sorted(MatchDetails_captains,key=get_val,reverse=True):
                
             print(key,"\t\t",MatchDetails_captains[key][0],"\t\t\t",MatchDetails_captains[key][1],"\t\t\t",MatchDetails_captains[key][2])

                
def get_val(key):
        return MatchDetails_captains.get(key)



MatchDetails_captains={}
with open ("captains.txt",mode='r') as file:
                 header=next(file)
                 match_array()
