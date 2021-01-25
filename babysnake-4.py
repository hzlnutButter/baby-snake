from datetime import datetime

people_dict = {} # name_input: [Persons]

def get_first_name(name_input):
    first_name = ""
    for char in name_input:
        if char == " ":
            break
        else:
            first_name += char
    return first_name

def get_chart_block(output, num): # returns 30char + "|"
    if len(output) > 20:
        output = output[:18] + "."
    elif len(output) < 1:
        output = str(num) + "/10"
    total_spaces = 30 - len(output)
    side1 = int(total_spaces / 2)
    if (total_spaces % 2) == 0:
        side2 = side1
    else:
        side2 = side1 + 1
    return (" " * side1) + output + (" " * side2) + "|"

class Person:
    def __init__(self, name_input):
        self.name = name_input
        self.first_name = get_first_name(name_input)
        self.feelings = {} # datetime: [float, string]
    def __repr__(self):
        return self.name
    def update_feeling(self): # TO DO: make the rating out of 10 always an int? not ipmortant
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
        timestamp = datetime.now().strftime("%b %d %H:%M:%S")
        self.feelings[timestamp] = feelings_list
        return feelings_list
    def show_chart(self):
        timestamps_line = "\n    |"
        empty_line = "    |"
        dict_of_levels = {10: "10: |", 9: " 9: |", 8: " 8: |", 7: " 7: |", 6: " 6: |", 5: " 5: |", 4: " 4: |", 3: " 3: |", 2: " 2: |", 1: " 1: |"}

        for timestamp in self.feelings:
            num_feel = round((self.feelings[timestamp])[0]) # nearest int from 1 to 10
            str_feel = (self.feelings[timestamp])[1] # an adjective

            timestamps_line += get_chart_block(timestamp, 0)
            empty_line += get_chart_block(" ", 0)

            dict_of_levels[num_feel] += get_chart_block(str_feel.upper(), num_feel)

            for level in dict_of_levels: # adds spaces to all remaining lines
                if level == num_feel:
                    continue
                else:
                    dict_of_levels[level] += ((" " * 30) + "|")
        
        print(timestamps_line)
        print(empty_line)
        for level in dict_of_levels:
            print(dict_of_levels[level])
        print("\n")
    def get_feelings_list(self):
        feelings_list = []
        for key in self.feelings:
            values = self.feelings[key]
            feelings_list.append(values)
        return feelings_list

        #self.feelings = {} # datetime: [float, string]

def i_know_you(name_input):
    for person_i_know in people_dict:
        if person_i_know == name_input:
            have_met_input = input("hmm... that sounds familiar, have we met?  ").lower()
            while True:
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

def get_which_person(name_input): # only called after "i_know_you" returns True. if Person isn't found, returns None
    possible_people = people_dict[name_input] # list of Persons
    for possible_person in possible_people:
        feelings_list = possible_person.get_feelings_list()
        last_meeting = feelings_list[-1] # [float, string]
        is_right_person = input("last time we spoke, did you say you were " + last_meeting[1].upper() + " and rate yourself " + str(last_meeting[0]) + "/10?  ")
        while True:
            if is_right_person[0].lower() == "y":
                return possible_person
            elif is_right_person[0].lower() == "n":
                break
            else:
                print("um, yes or no please. is that you?  ")
    return

while len(people_dict) < 10:
    name_input = input("\nhey there! what's your name?  ").lower()
    first_name = get_first_name(name_input)
    new_person = True

    num_friends = 0
    for key in people_dict:
        for person in people_dict[key]:
            num_friends += 1

    if i_know_you(name_input):
        right_person = get_which_person(name_input)
        if right_person is None:
            print("well, that's all i've got. i must not have met you before.")
            person = Person(name_input)
            num_friends += 1
        else:
            person = right_person
            new_person = False
    else:
        person = Person(name_input)
        num_friends += 1
        print("great to meet you, " + first_name + "! i'm baby snake.")
    
    if num_friends == 1:
        num_friends_str = str(num_friends) + " friend!"
    else:
        num_friends_str = str(num_friends) + " friends!"
    
    print("guess what, " + first_name + "? i've got " + num_friends_str)
    feelings_list = person.update_feeling() # [float, string]
    
    person.show_chart()
    
    if new_person:
        if name_input in people_dict:
            people_dict[name_input].append(person)
        else:
            people_dict[name_input] = [person]

    # TO DO: deal with empty inputs
    # TO DO: allow termination message at any time
    # TO DO: make it clear who says what when

# termination message
if len(people_dict) >= 10:
    print("ahhhh i have too many friends, time to die.")
else:
    print("i have been erased. i hope you know what you have done.")