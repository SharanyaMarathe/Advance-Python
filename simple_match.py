import re
data="jhg jhgc the kjh uythe"
match=re.search(r"the",data)
if match:
    print("found",match.group())
else:
    print("not found")
