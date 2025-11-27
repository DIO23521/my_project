# 1. create a counter that counts custom amount(✅) in custom intervals(✅) and then print something may be random
#                                                                                                      from list(✅)
# add input for question(✅)
# do it repeatable  and closable(✅)

import time
import random
from tarot_list import *



def question_input():

    question = input("Enter your question: ")

    while True:
#                   do question completely alphabetical if used only " " or "?"
#            (and if temp question is completely alphabetical - push question with " " and "?" to (else))
#                                            ⬇️
        temporary_question = question.replace(" ", "").replace("?", "")

        if len(question) > 40:
            print("Your ques cant be more than 40 characters")
            question = input("Enter your question: ")         # new assign every time because
                                                              # I need new answer every loop
        elif question.count("?") != 1:
            print("Your question must contain only one '?'")
            question = input("Enter your question: ")
#
#      Check whether the temp_question is completely alphabetical
#                         ⬇️
        elif not temporary_question.isalpha():
            print("You cant use signs except spaces and question mark")
            question = input("Enter your question: ")

        else:
            print(f"Your question is '{question}'")
            break

    return question    # return allows you to pass the final, validated value of a variable
                    # from the internal environment of a function to the outside, where you called the function.




def add_num():

    while True:
        try:
            range_num = int(input("Enter a range number: "))
            while True:
                if range_num < 0:
                    range_num = int(input("Enter not a negative range number: "))
                else:
                    break

        except ValueError:
            print("only numbers")
            continue
        return range_num




def custom_time():

    time_for_sleep = 0

    while time_for_sleep not in range(1, 11):
        try:
            time_for_sleep = int(input("Enter the number of seconds for the interval between counts (1-10): "))
        except ValueError:
            print("invalid option")
            continue

    return time_for_sleep




def main():
    while True:

        your_question = question_input()
        added_num = add_num()
        amount_time = custom_time()

        for num in range(added_num):
            time.sleep(amount_time)
            print(num)
        print(random.choice(tarot_cards))
        print(f"Your question was '{your_question}'")

        while True:

            continue_game = input("Do you want to play again? (y/n): ").lower()

            if continue_game == "y":
                break
            elif continue_game == "n":
                break
            else:
                print("Invalid input")
                continue

        if continue_game == "n":
            break

    print("Thanks for playing!😊")




if __name__ == '__main__':
    main()