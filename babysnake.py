#!/usr/local/bin/python3

from datetime import datetime
import time
from os import system # commands work for mac terminal, not windows

system("clear")

people_dict = {} # {name_input: [p1, p2...]}

def delay_print(output):
    pace = .03
    for char in output:
        print(char, end="", flush=True)
        time.sleep(pace)
        if pace > .005:
           pace = pace - .001
    print("")

def get_input(output): # returns processed input
    delay_print(output)
    user_input = input(" --> ").strip().lower()
    while True:
        if user_input:
            if "obliviate" in user_input:
                delay_print("\nself-destruct has been triggered...")
                delay_print("i am now self-destructing.\n")
                exit()
            else:
                return user_input
        else:
            delay_print("hmm... i don't think that was an answer.")
            user_input = input(" --> ")

def get_first_name(name_input):
    first_name = ""
    for char in name_input:
        if char == " ":
            break
        else:
            first_name += char
    return first_name

def set_password(person): # sets password and changes user status ("logs in")
    password = get_input("please set a password so I know who you are.")
    past_people = people_dict[person.name] # list of Persons
    list_of_passwords = []
    for past_person in past_people:
        list_of_passwords.append(past_person.password)
    while True:
        if password in list_of_passwords:
            password = get_input("sorry, that password is unavailable. try another.")
        else:
            person.set_password(password)
            delay_print("\n*logging in as " + name_input.upper() + "*\n")
            return

def get_chart_block(output, num): # returns 30char + "|"
    if len(output) > 20:
        output = output[:18] + "."
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
        self.password = ""
        self.memories = {}
    def __repr__(self):
        return self.name
    def set_password(self, password):
        self.password = password
    def update_feeling(self):
        self.num_feel = get_input("let's update your mood chart. how are you on a scale from 1 to 10?")
        while True: # checks type "float" and range
            try:
                self.num_feel = float(self.num_feel)
                if self.num_feel < 1 or self.num_feel > 10:
                    self.num_feel = float(get_input("it has to be between 1 and 10."))
                else:
                    break
            except ValueError:
                self.num_feel = get_input("uh, that doesn't look like a number.")
                continue
        self.str_feel = get_input("describe your mood in one word.")
        feelings_list = [self.num_feel, self.str_feel]
        timestamp = datetime.now().strftime("%b %d %H:%M:%S")
        self.feelings[timestamp] = feelings_list
        return feelings_list
    def show_chart(self):
        delay_print("here's your mood chart:")
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

def i_know_you(name_input):
    for person_i_know in people_dict:
        if person_i_know == name_input:
            have_met_input = get_input("hmm... that sounds familiar, have we met?")
            while True:
                if have_met_input[0] == "y":
                    delay_print("i thought i remembered you, " + get_first_name(name_input) + "!")
                    return True
                elif have_met_input[0] == "n":
                    delay_print("must have been a different " + name_input + ".")
                    return False
                else:
                    have_met_input = get_input("um, yes or no please. have we met before?")
    return False

def get_which_person(name_input): # returns a Person, or None
    password_input = get_input("please enter your password.")
    possible_people = people_dict[name_input] # list of Persons
    while True:
        for possible_person in possible_people:
            if password_input == possible_person.password:
                return possible_person
        password_input = get_input("password is incorrect. try again.")
    return

def add_memory(person):
    delay_print("what would you like me to remember?")
    memory = input(" --> ")
    while True:
        if memory:
            break
        else:
            delay_print("unfortunately, i can't store nothing. try again.")
            memory = input("")
    memory_type = get_input("and what name should we use to refer to this memory?")
    if memory_type in person.memories:
        overwrite = get_input("i've already stored something by that name. would you like to overwrite it?")
        while True:
            if overwrite[0] == "y":
                delay_print("ok! i'll save " + memory.upper() + " with the title " + memory_type.upper() + ".")
                person.memories[memory_type] = [memory]
                break
            elif overwrite[0] == "n":
                delay_print("ok! i'll add " + memory.upper() + " to the existing memory titled " + memory_type.upper() + ".")
                (person.memories[memory_type]).append(memory)
                break
            else:
                overwrite = get_input("i'm gonna need a 'yes' or a 'no'.")
    else:
        delay_print("ok! i'll save " + memory.upper() + " with the title " + memory_type.upper() + ".")
        person.memories[memory_type] = [memory]

def give_memory(person):
    memory_type = get_input("what's name of the memory you want to be reminded of?")
    memory_string = ""
    if memory_type in person.memories:
        for item in person.memories[memory_type]:
            memory_string += (str(item) + ", ")
        memory_string = memory_string.strip()
        memory_string = memory_string.strip(",")
        delay_print(memory_type.upper() + ": " + memory_string)
    else:
        delay_print("i don't have a memory by that name.")

# # # #
# beginning of main loop
# # # #

while True:
    name_input = get_input("\nhey there! what's your name?")
    first_name = get_first_name(name_input)
    new_person = True

    num_friends = 0
    for each_name in people_dict:
        for each_person in people_dict[each_name]:
            num_friends += 1

    if i_know_you(name_input):
        right_person = get_which_person(name_input)
        if right_person is None:
            delay_print("huh. we must not have met after all.")
            person = Person(name_input)
            num_friends += 1
        else:
            person = right_person
            new_person = False
            delay_print("\n*logging in as " + name_input.upper() + "*\n")
    else:
        person = Person(name_input)
        num_friends += 1
        delay_print("great to meet ya! i'm baby snake.")
    
    if new_person:
        if name_input in people_dict:
            people_dict[name_input].append(person)
        else:
            people_dict[name_input] = [person]
        set_password(person)

    num_friends_str = str(num_friends) + (" friend!" if num_friends == 1 else " friends!")
    
    delay_print("guess what, " + first_name + "? i have " + num_friends_str)
    feelings_list = person.update_feeling() # [float, string]
    person.show_chart()

    while True:
        delay_print("enter a number if you would like me to do anything else, or press 'return' to log out.")
        delay_print("\n1.  STORE A PIECE OF INFORMATION IN MY MEMORY\n2.  RETRIEVE A PIECE OF INFORMATION IN MY MEMORY")
        what_next = (input("\n --> ").strip())
        if not what_next:
            break
        elif what_next == "1":
            add_memory(person)
        elif what_next == "2":
            if len(person.memories) == 0:
                delay_print("you don't have any stored memories.")
                continue
            else:
                give_memory(person)

    delay_print("\nsee you next time! *logging out*")
    time.sleep(1.5)
    system('clear')

    # TO DO: if a memory that the user wants to recall isn't found, give the option to add it right away in give_memory