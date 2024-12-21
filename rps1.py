import random

emoji = {"r":"🪨🪨🪨🪨🪨","p":"📜📜📜","s":"✂️✂️✂️✂️"}
select = ("r","s","p")

while True:
    user_choice = input("Choose: rock (r), paper (p), or scissors (s): ").lower()

    if user_choice not in select:
        print("this is invalide")
        

    computer_input = random.choice(select)


    print (f'you choose {emoji[user_choice]}') ### user input 
    print (f'compurter input {emoji[computer_input]}') #### computer input 

    if user_choice == computer_input:
        print("You both entered the same, it's a Tie 🤞🤞🤞")
    elif (user_choice == "s" and computer_input == "p") or \
        (user_choice == "r" and computer_input == "s") or \
        (user_choice == "p" and computer_input == "r"):
        print("You win!👍👍👍👍")
    else:
        print("You lose!😞😞😞😞")

    play_again = input(" would you like paly  (y/n);?").lower()

    if play_again not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue  # Ask again

    if play_again == 'n':
            print("Thanks for playing! Hope you had fun! ❤️❤️❤️")
            break  # Exit the loop if user chooses 'n'














