def divide_one(remainder, divisor):
    quotient = 0b0000000000000000

    print(f"{'Iter.':^5} {'Remainder':<10}{'Divisor':<10}{'Quotient':<10}")

    for x in range(1, 9):
        print(f"{x:^5} {bin(remainder)[2:].zfill(8):<10}{bin(divisor)[2:].zfill(8):<10}"
              f"{bin(quotient)[2:].zfill(4):<10}")

        remainder = remainder - divisor

        if remainder > 0b0:
            quotient = (quotient << 1) | (1 << 0)

        elif remainder < 0b0:
            remainder = remainder + divisor
            quotient << 1

        elif remainder == 0b0:
            return

        divisor = divisor >> 1

    return


def divide_two():
    pass
