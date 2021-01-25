people_dict = {} #stores ("name" var) : (Person obj)

def get_first_name(name_input):
    first_name = ""
    for char in name_input:
        if char == " ":
            break
        else:
            first_name += char
    return first_name

class Person:
    def __init__(self, name_input):
        self.name = name_input
        self.first_name = get_first_name(name_input)
    def __repr__(self):
        return self.name
    def update_feeling(self):
        self.num_feel = input("how are you right now on a scale from 1 to 10?  ")
        while True: # checks type "int"
            try:
                self.num_feel = int(self.num_feel)
            except ValueError:
                self.num_feel = input("uh, i don't think that was a number. try again?  ")
                continue
            break
        if self.num_feel < 1:
            self.num_feel = 1
            print("well, that's a low number. sorry to hear it. i'm gonna count that as a 1/10.")
        elif self.num_feel > 10:
            self.num_feel = 10
            print("off the charts! glad to hear it. i'm gonna count that as a 10/10.")
        return self.num_feel

def i_know_you(name_input):
    for person_i_know in people_dict:
        if person_i_know == name_input:
            have_met_input = input("hmm... that sounds familiar, have we met?  ").lower()
            have_met = None
            while have_met is None:
                if have_met_input[0] == "y":
                    print("i thought i remembered you, " + get_first_name(name_input) + "!")
                    return True
                elif have_met_input[0] == "n":
                    print("must have been a different " + name_input + ".")
                    return False
                else:
                    print("um, yes or no please. have we met before?  ")
        else:
            return False

while len(people_dict) < 10:
    name_input = input("\nhey there! what's your name?  ").lower()
    first_name = get_first_name(name_input)
    
    if i_know_you(name_input):
        person = people_dict[name_input]
        num_friends = len(people_dict)
    else:
        person = Person(name_input)
        num_friends = len(people_dict) + 1
        print("great to meet you, " + first_name + "! i'm baby snake.")
    
    if num_friends == 1:
        num_friends_str = str(num_friends) + " friend!"
    else:
        num_friends_str = str(num_friends) + " friends!"
    
    print("guess what, " + first_name + "? i've got " + num_friends_str)
    num_feel = person.update_feeling()

    people_dict[name_input] = person

# termination message
if len(people_dict) >= 10:
    print("ahhhh i have too many friends, time to die.")