from adr import get_name, get_dob
from adr import get_city, get_vehicle,new_rule_dec

def gen_license(adhr_id):
    person_name = get_name(adhr_id)
    person_dob = get_dob(adhr_id)
    person_city = get_city(adhr_id)
    print(f"""   -- LICENSE --
    Name          : {person_name}
    Date of Birth : {person_dob}
    Place         : {person_city}
    """)

def gen_rc_book(adhr_id):
    person_name = get_name(adhr_id)
    person_vnum = get_vehicle(adhr_id)
    person_city = get_city(adhr_id)
    print(f"""   -- RC Book --
    Name          : {person_name}
    Place         : {person_city}
    Vehicle Num   : {person_vnum}
    """)

# Main
aadhaar_number = u'\u0ce9'
#get_name=wrapper
#get_name=new_rule_dec(get_name)
#(By adding @decorator name(wrapper) in adr.py the repitation of these lines are avoided

gen_license(aadhaar_number)
gen_rc_book(aadhaar_number)
