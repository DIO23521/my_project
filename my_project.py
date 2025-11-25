# 1. create a counter that counts custom amount(✅) in custom intervals(✅) and then print something may be random
#                                                                                                      from list(✅)
# add input for question(⌛)
# do it repeatable  and closable(⌛)

import time
import random
from tarot_list import *


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


#

def main():
    added_num = add_num()
    amount_time = custom_time()

    for num in range(added_num):
        time.sleep(amount_time)
        print(num)
    print(random.choice(tarot_cards))


if __name__ == '__main__':
    main()