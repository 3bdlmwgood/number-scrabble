# File: CS112_A1_T2_2_20230230.py
# Purpose: Number Scrabble is a simple game between two players who choose numbers from 1 to 9 to get 3 numbers whose total sum is 15
# Author: [Abdallah Mohamed Abdelmawgood]
# ID: [20230230]

def number_scrabble():
    print("** Welcome to Number Scrabble **")
    player1 = input("Please enter the name of the first player: ")
    player2 = input("Please enter the name of the second player: ")
    print("\nLet's play ^⁠_⁠^!\n")

    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player1_choices = []
    player2_choices = []         # no numbers for players Firstly

    while True:

        print("Available numbers :", num_list)  #To make it easier for the first player to see the list updated
        
        #player1
        num1 = int(input(player1 + ", choose a number from the list: "))
        while num1 not in num_list:
            print("Invalid choice. Please select a number from the available list:",num_list)
            num1 = int(input(player1 + ", choose a number from the list: "))
        num_list.remove(num1)
        player1_choices.append(num1)
        print("Numbers chosen by", player1 + ":", player1_choices)
        if check_win(player1_choices):
            print("Congratulations", player1 + "! You reach 15. You win!")
            break
        elif len(player1_choices) == 5:
            print("Game over! No player reached 15. It's a draw.")
            break

        print("Available numbers :", num_list)   #To make it easier for the second player to see the list updated
        
        #player2
        num2 = int(input(player2 + ", choose a number from the list: "))
        while num2 not in num_list:
            print("Invalid choice. Please select a number from the available list:",num_list)
            num2 = int(input(player2 + ", choose a number from the list: "))
        num_list.remove(num2)
        player2_choices.append(num2)
        print("Numbers chosen by", player2 + ":", player2_choices)
        if check_win(player2_choices):
            print("Congratulations", player2 + "! You reach 15. You win!")
            break
        elif len(player2_choices) == 5:
            print("Game over! No player reached 15. It's a draw.")
            break

def check_win(choices):
    if len(choices) == 3 and sum(choices) == 15:
        return True
    elif len(choices) == 4:
        for a in range(4):  # a from first[0] number to fourth number[3] 
            for b in range(a+1,4):   # b from second number [1] to fourth number [3]  
                for c in range(b+1,4):   # c from third number [2] to fourth number [3]
                    if choices[a]+choices[b]+choices[c]==15:   # Check the probability of the sum of the three numbers being 15
                        return True
    elif len(choices) == 5:
        for a in range(5):
            for b in range(a+1,5):
                for c in range(b+1,5):
                    if choices[a]+choices[b]+choices[c]==15:
                        return True
    return False

number_scrabble()
