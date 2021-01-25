from datetime import datetime

people_dict = {} # name_input: Person

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
        self.feelings = {} # datetime: [float, string]
    def __repr__(self):
        return self.name
    def update_feeling(self):
        self.num_feel = input("how are you right now on a scale from 1 to 10?  ")
        while True: # checks type "float"
            try:
                self.num_feel = float(self.num_feel)
            except ValueError:
                self.num_feel = input("uh, i don't think that was a number. try again?  ")
                continue
            break
        if self.num_feel < 1:
            self.num_feel = 1
        elif self.num_feel > 10:
            self.num_feel = 10
        self.str_feel = input("can you give me an adjective to describe that?  ")
        feelings_list = [self.num_feel, self.str_feel]
        self.feelings[datetime.now()] = feelings_list
        return feelings_list
    def show_chart(self):
        num_instances = len(self.feelings)

        for instance in self.feelings:
            timestamp = instance.strftime("%b %d %H:%M")
            list_feel = self.feelings[instance]
            num_feel = list_feel[0]
            str_feel = list_feel[1]
            # show the adjective on a row according to its numerical value
            # round the float to the nearest whole number
        

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
    if "obliviate" in name_input:
        break
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
    feelings_list = person.update_feeling() # [float, string]
    if feelings_list[0] < 4:
        print("sorry you're " + feelings_list[1] + "! wish there was something i could do :(")
    elif feelings_list[0] >= 7:
        print("glad to hear you're " + feelings_list[1] + ".")
    # if len(feelings_list) > 1:
        # offer to show a chart??

    people_dict[name_input] = person

# termination message
if len(people_dict) >= 10:
    print("ahhhh i have too many friends, time to die.")
else:
    print("i have been erased. i hope you know what you have done.")