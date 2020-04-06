from get_lines_gen import get_lines,get_parts,get_filtered
from sys import getsizeof

with open("captains.txt") as FH:
    all_lines=get_lines(FH)
    print("data size: ",getsizeof(all_lines),"bytes")
    individuals=get_parts(all_lines)
    print("data size: ",getsizeof( individuals),"bytes")
    captains_since2000=get_filtered(individuals)
    print("data size: ",getsizeof(captains_since2000),"bytes")
    for line in captains_since2000:
        print(line)
