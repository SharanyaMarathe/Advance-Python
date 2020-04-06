import calci
import sys
Aus_runs1=int(sys.argv[1])
India_runs1=int(sys.argv[2])
Aus_runs2=int(sys.argv[3])
Aus_total=calci.add(Aus_runs1,Aus_runs2)
India_runs2=calci.sub(Aus_total,India_runs1)
India_total=calci.add(India_runs2,1)
print("India should score:  ",India_total)
