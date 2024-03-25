attendees = input("Enter number of attendees: ")
attendees = int(attendees) #missing int converstion
venue = "large hall" if attendees > 100 else "conference room"
print(venue)