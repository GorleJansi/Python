while True:                            #  infinite loop - condition True never becomes False on its own ,changr manually(break)
    name = input("Enter 'q' to quit: ")
    if name == "q":
        break
#Explicit infinite loop; you forcefully exit with break.

x = ""   # initialize variable
while x != "q":   # loop continues until user enters "q"
    x = input("Enter 'q' to quit: ")


#Loop ends naturally when condition is False.