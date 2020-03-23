import math


def solve_square_equation(a, b, c):
    result = []
    ax = None
    bx = None
    cx = None

    result.append("")
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
    result.append(f"{ax + bx + cx} = 0")
    result.append(f"a = {a}; b = {b}; c = {c}.")
    D = (b ** 2) - (4 * a * c)
    result.append(f"D = {b ** 2} - 4 * {a} * {c} = {D}")
    if D > 0:
        x1 = float((-b + math.sqrt(D)) / (2 * a))
        x2 = float((-b - math.sqrt(D)) / (2 * a))
        result.append(f"x1 = ({-b} + {float(math.sqrt(D))}) / (2 * {a}) = {x1}\n"
                      f"x2 = ({-b} - {float(math.sqrt(D))}) / (2 * {a}) = {x2}")
    elif D == 0:
        x = -b / 2 * a
        result.append(f"x = {-b} / 2 * {a} = {x}")
    elif D < 0:
        result.append("x = {0}")
    result.append("---")
    return result


if __name__ == "__main__":
    while True:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        for line in solve_square_equation(a, b, c):
            print(line)
