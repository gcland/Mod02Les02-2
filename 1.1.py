place = input("Choose a place: forest or cave? ")
#no else statement for what happens if forest or cave not entered. If 'forest' or 'cave' typed incorretly by user (e.g. with additional space or captialization), code does not work. 
#Should be fixed but probably not necessary for this assignment.
if place == "forest": #missing second '='.
    action = input("climb a tree or cross a river?")
    if action == "climb a tree": #missing second '='. 
        #adding a space at the end of 'climb a tree ' resulted in else statement triggering; should be fixed but probably not necessary for this assignment.
        print("You found a bird's nest!")
    else: #statements in else not allowed.
        print("You found a boat!")
elif place == "cave": #missing second '='.
    print("You find a hidden treasure!")

else:
    pass