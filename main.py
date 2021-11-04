from BinaryMath.division import divide_one
from BinaryMath.multiplication import multiply_one


def main():
    menu = "\n" \
           "1) Multiplication Algorithm One\n" \
           "2) Multiplication Algorithm Two\n" \
           "3) Division Algorithm One\n" \
           "4) Division Algorithm Two\n" \
           "0) Quit\n"

    choice = -1

    # print(bin(int('1010', 2)))

    while True:
        try:
            print(menu)
            choice = int(input("Choice :> "))

            if choice == 1:
                multiplicand = int(input("Enter multiplicand:> "), 2)
                multiplier = int(input("Enter multiplier:> "), 2)
                multiply_one(multiplicand, multiplier)
            elif choice == 2:
                print("Choice 2")
            elif choice == 3:
                remainder = int(input("Enter remainder:> "), 2)
                divisor = int(input("Enter divisor:> "), 2)
                divide_one(remainder, divisor)
            elif choice == 4:
                print("Choice 4")
            else:
                if choice == 0:
                    return
                else:
                    print("Enter a integer between 0-4.")

        except ValueError:
            print("Invalid Input.")


if __name__ == "__main__":
    main()
