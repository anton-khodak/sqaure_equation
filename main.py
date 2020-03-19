import math
while True:
    ax = None
    bx = None
    cx = None
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print("")
    if a == 1:
        ax = "x²"
    elif a == -1:
        ax = "-x²"
    else:
        ax = f"{a}x²"
    if b == 1:
        bx = " + x"
    elif b > 0 and b != 1:
        bx = f" + {b}x"
    elif b == 0:
        bx = ""
    elif b == -1:
        bx = "- x"
    elif b < 0 and b != -1:
        bx = f" - {abs(b)}x"
    if c > 0:
        cx = f" + {c}"
    elif c == 0:
        cx = ""
    elif c < 0:
        cx = f" - {abs(c)}"
    print(f"{ax + bx + cx} = 0")
    print(f"a = {a}; b = {b}; c = {c}.")
    D = (b ** 2) - (4 * a * c)
    print(f"D = {b ** 2} - 4 * {a} * {c} = {D}")
    if D > 0:
        x1 = float((-b + math.sqrt(D)) / (2 * a))
        x2 = float((-b - math.sqrt(D)) / (2 * a))
        print(f"x1 = ({-b} + {int(math.sqrt(D))}) / (2 * {a}) = {x1}\n"
              f"x2 = ({-b} - {int(math.sqrt(D))}) / (2 * {a}) = {x2}")
    elif D == 0:
        x = -b / 2 * a
        print(f"x = {-b} / 2 * {a} = {x}")
    elif D < 0:
        print("x = {0}")
    print("---")
    continue
