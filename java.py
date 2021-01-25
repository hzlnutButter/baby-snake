people_list = [] #list of dictionaries

def get_first_name(name):
    first_name = ""
    for letter in name:
        if letter == " ":
            break
        else:
            first_name += letter
    return first_name

def get_met_bool():
    met_bool = None
    while met_bool is None:
        met_or_no = input("have we met before?  ").lower()
        if met_or_no[0] == "y":
            met_bool = True
        elif met_or_no[0] == "n":
            met_bool = False
        else:
            print("uh, yes or no answer please...")
            continue
    return met_bool

while len(people_list) < 10:
    name = input("\nhey there! what's your name?  ").lower()
    first_name = get_first_name(name)
    met_bool = False
    person = {}
    
    if "end" in name:
        break
    for people in people_list:
        if people["name"] == name:
            met_bool = get_met_bool()
            if met_bool == True:
                print("thought so!")
                person = people
            else:
                print("oh, my bad! must have been a different " + first_name + ".")
            break
    if met_bool == True:
        print("it's great to see you again, " + first_name + ".")
    else:
        person["name"] = name
        if len(people_list) + 1 == 1:
            num_friends = str(len(people_list) + 1) + " friend!"
        else:
            num_friends = str(len(people_list) + 1) + " friends!"
        print("i'm baby snake. guess what, " + first_name + "? i now have " + num_friends)
        
        num_feel = input("how are you on a scale from 1 to 10?  ")
        feeling = input("\n")
        
        people_list.append(person)

print("\nokay, i need a break now.")