from textwrap import dedent
# -------------------------------------------------------------------------------- #
def Mod(A, B):
    B0 = B
    I = 1
    # -------------------------------------------------------------------------------- #
    while True:
        B = B0 * I
        C = B + B0
        if C > A: break
        else: I += 1
    R = A - B
    # -------------------------------------------------------------------------------- #
    display = dedent("""
        Steps:
        1) {1} x {3} = {4}
        2) {0} - {4} = {2}
        
        Remainders = {2}""")
    print(display.format(A, B0, R, I, B))
# -------------------------------------------------------------------------------- #
def InverseMod(A, B):
    I = 1
    # -------------------------------------------------------------------------------- #
    while True:
        X = (B * I) + 1
        Y = X / A
        if float.is_integer(Y): break
        else: I += 1
        # -------------------------------------------------------------------------------- #
    Y = int(Y)
    display = dedent("""
        Steps:
        1) {0} x {1} = {2}
        2) {2} + 1 = {3}
        3) {3} / {4} = {5}
        
        Answer = {5}""")
    print(display.format(B, I, (X - 1), X, A, Y))
# -------------------------------------------------------------------------------- #
while True:
    for x in range(80): print('-', end='')
    else: print()
    # -------------------------------------------------------------------------------- #
    menu = dedent("""
        [1] Mod Algorithm
        [2] Inverse Mod Algorithm
        [3] Exit
         >> """)
    inp = input(menu)

    if inp == '1' or inp == '2':
        A = str(input("Enter A: "))
        isA = A.isnumeric()
        B = str(input("Enter B: "))
        isB = B.isnumeric()

        if isA and isB:
            A = int(A)
            B = int(B)
            Mod(A, B) if inp == '1' else InverseMod(A, B)
        else: print("Error 2! Enter Numbers")
    elif inp == '3': break
    else: print("Error 1! Input Correctly")
print("Bye")
# -------------------------------------------------------------------------------- #