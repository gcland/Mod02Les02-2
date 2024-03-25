place = input("Choose a place: forest or cave? ")

if place == "forest": 
    action = input("climb a tree or cross a river?")
    if action == "climb a tree": 
        print("You found a bird's nest!")
    else: 
        print("You found a boat!")
elif place == "cave":
    action = input("Do you light a torch? Or proceed in the darkness...")
    if action == "light a torch":
        print("The torch's glow startles the bats in the cave, becoming alarmed and flying throughout the cave!")
        print("Some of the bats swarm you and scratch your face! One of them had rabies and you did not get your rabbies vaccine! You died.")
    else:
        print("You hear the chittering of bats within the cave and decide to proceed in the darkness.")
        print("You notice a stuble glow in the near distance and make your way to it to discover a hidden treasure!")

else:
    pass