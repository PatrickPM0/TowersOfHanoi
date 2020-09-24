"""
Program to recursively solve the towers of hanoi of any size.
"""


def print_move(fr, to):
    print(f"{fr} moves to {to}")


def Towers(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)


if __name__ == "__main__":
    blocks_number = int(input("How many blocks on the first tower?"))
    Towers(blocks_number, 'P1', 'P2', 'P3')
