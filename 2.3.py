attendees = input("Enter number of attendees: ")
attendees = int(attendees) #missing int converstion
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
facilities = "audio system and projector" if attendees > 50 else "projector"
print(facilities)

food = input("Would you like vegetarian food? ")
if food == "yes":
    print("I recommend Veggie Delight Caterers for vegetarian food.")
elif food == "Yes":
    print("I recommend Veggie Delight Caterers for vegetarian food.")

else:
    print("I recommend Gourmet Meals Caterers if you would not like vegetarian food.")