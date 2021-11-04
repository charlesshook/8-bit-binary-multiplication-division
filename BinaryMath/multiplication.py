def multiply_one(multiplicand, multiplier):
    product = 0b0000000000000000

    print(f"{'Iter.':^5} {'Multiplier':<12}{'Multiplicand':<15}{'Product':<18}")

    for x in range(1, 9):
        if 0b0 != multiplier:
            print(f"{x:^5} {bin(multiplier)[2:].zfill(8):<12}{bin(multiplicand)[2:].zfill(8):<15}"
                  f"{bin(product)[2:].zfill(16):<18}")

            product = product + multiplicand
            multiplicand = multiplicand << 1
            multiplier = multiplier >> 1
        else:
            print(f"{x:^5} {bin(multiplier)[2:].zfill(8):<12}{bin(multiplicand)[2:].zfill(8):<15}"
                  f"{bin(product)[2:].zfill(16):<18}")

            return


def multiply_two(multiplicand, multiplier):
    product = 0b0000000000000000

    print(f"{'Iter.':^5}{'Multiplier':^12}{'Multiplicand':^14}{'Product':^18}")

    print(f"{iter:^5}{bin(multiplier)[2:]:^12}{bin(multiplicand)[2:]:^14}{bin(product)[2:]:^18}")
