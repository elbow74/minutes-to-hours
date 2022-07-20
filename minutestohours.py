
def question():
    print("Which one would you like to convert today: \n 1. minutes to hours \n 2. hours to minutes")
    choice_input = input("Input 1 or 2: ")
    if choice_input == 1:
        minutes_amount = input("How many minutes has it been: ")
        time = int(minutes_amount)
        time = time / 60
        print(str(time) + " hours")
    elif choice_input == 2:
        hours_amount = input("How many hours has it been: ")
        time = int(hours_amount)
        time = time * 60
        print(str(time) + " minutes")


question()
