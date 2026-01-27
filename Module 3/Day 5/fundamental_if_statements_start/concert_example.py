concert_name = input("What is the name of the concer tonight?")
has_ticket = input("Do you have a ticket? (y/n)")

if has_ticket == "y":
    if concert_name == "taylor swift":
        print("You're in the right place!")
        print("Have Fun!")
    elif concert_name == "blink 182":
        print("Your concert is next door ->")
    elif concert_name == "taylor swift":
        print("Do you want to buy a ticket?")
    else:
        print("This is not the concert you're looking for :(")
else:
    print("Please see the box office for tickets.")