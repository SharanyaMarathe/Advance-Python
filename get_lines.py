def get_lines(FH):
    lines=list()
    for line in FH:
        lines.append(line)

    return lines

def get_parts(dlist):
    dparts=list()
    for sent in dlist:
        parts=sent.split(',')
        dparts.append(parts)

    return dparts

def get_filtered(info):
    subset=list()
    for ele in info:
        if '20' in ele[1]:
            subset.append((ele[1],ele[0]))
            
    return subset
