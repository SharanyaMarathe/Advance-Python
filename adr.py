'''def wrapper(adhr_id):
    nums={ u'\u0ce7' : 1,
           u'\u0ce8' : 2,
           u'\u0ce9' : 3}
    id_num=nums[adhr_id]
    msg=get_name(id_num)
    msg=msg.upper()
    return msg'''
def new_rule_dec(func):
    def wrapper(adhr_id):
        nums={ u'\u0ce7' : 1,
               u'\u0ce8' : 2,
               u'\u0ce9' : 3}
        id_num=nums[adhr_id]
        msg=func(id_num)
        msg=msg.upper()
        return msg
    
    return wrapper
   
@new_rule_dec
def get_name(adhr_id):
    # Connect to DB
    # Assume we get the below list 
    # as a response to a DB query
    names = [ "Ajay", "Vishal", 
              "Girish", "Dinesh" ]
    # Disconnect from DB
    name = names[adhr_id]
    return name

@new_rule_dec
def get_city(adhr_id):
    #pass
    return "Belgaum"

def get_dob(adhr_id):
    return "1-1-1970"

def get_vehicle(adhr_id):
    return "KA01 AB 007"
