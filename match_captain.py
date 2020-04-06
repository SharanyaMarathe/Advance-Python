from reg_getlines_gen import get_lines,get_parts,get_filtered,get_names
with open("captains.txt") as FH:
    all_lines=get_lines(FH)
    #for ele in all_lines:
       #print(ele)
    captains_name=get_names(all_lines)
    for names in captains_name:
            print(names)
    print("*********************")
with open("captains.txt") as FH:
    all_lines=get_lines(FH)    
    individuals=get_parts(all_lines)
    captains_2000=get_filtered(individuals)
    for C_names in captains_2000:
        print(C_names)
