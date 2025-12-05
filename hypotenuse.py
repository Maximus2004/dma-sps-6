import math

def get_hypotenuse(a, b):
    return math.sqrt(math.pow(a, 3) + math.pow(b, 3))

if __name__ == "__main__":
    print("Введи а:")
    a = int(input())
    print("Введи b:")
    b = int(input())
    print("c =", get_hypotenuse(a,b))
