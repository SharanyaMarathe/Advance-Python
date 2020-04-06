import re
def get_lines(FH):
    lines=list()
    for line in FH:
          yield line
        #lines.append(line)

    #return lines

def get_names(dlist):
    dparts=list()
   # pattren=r'[A-Za-z]'
    for sent in dlist:
        match=re.search(r'[A-Za-z][\s][A-Za-z]*',sent)
        if match:
            yield match.group()
        #dparts.append(parts)
            
def get_parts(dlist):
    dparts=list()
    for sent in dlist:
        parts=sent.split(',')
        yield parts

    #return dparts

def get_filtered(info):
    subset=list()
    for ele in info:
        if '20' in ele[1]:
            yield (ele[1],ele[0])
            #subset.append((ele[1],ele[0]))
            
    #return subset
