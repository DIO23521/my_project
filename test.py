

while True:
    try:
        range_num = input("Enter a range number: ")

    except ValueError:
        if not range_num.isdigit():
            print("Enter valid number")
            continue
