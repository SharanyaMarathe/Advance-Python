def gen_num(start=0,end=0,incr=1):
 print("start: ",start)
 print("End: ",end)
 print("Incr: ",incr)

inputs={'start':30,'end':90,'incr':5}
outputs={'hello':5,'byee':4}
#res=list(map(gen_num,inputs))
gen_num(*inputs)
gen_num(**inputs)
all_dict={**inputs,**outputs}
print(all_dict)
 
