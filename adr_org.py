def get_name(adhr_id):
    # Connect to DB
    # Assume we get the below list 
    # as a response to a DB query
    names = [ "Ajay", "Vishal", 
              "Girish", "Dinesh" ]
    # Disconnect from DB
    name = names[adhr_id]
    return name

def get_city(adhr_id):
    #pass
    return "Belgaum"

def get_dob(adhr_id):
    return "1-1-1970"

def get_vehicle(adhr_id):
    return "KA01 AB 007"
