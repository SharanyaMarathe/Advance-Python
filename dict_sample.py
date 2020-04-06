batting_names={"harish":79,"sunnil":28,"ravi":30,"Giri":25,"mahesh":28,"yuvi":30}
bowling_names={}
k1=list()
for k,v in batting_names.items():
    if bowling_names.has_key(v):
       #k1.insert(0,k)
       bowling_names[v]=bowling_names[v]+" ," +k  
       #print(bowling_names[v])
    else:
         bowling_names[v]=k
         #print(bowling_names) 
'''bowling_names[v]=[keys,k]'''
print(bowling_names)

