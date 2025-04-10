def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        print("you cannot divide with 0")
        return
    return a / b
def power(x, y):
    return x ^ y
def mod(x, y):
    return x % y

def main():
    power(3,5)
    add(4,6)
    subtract(5, 8)
    multiply(74565, 214323423)
    mod(23423, 54)
    divide(65, 23)



if __name__ == "__main__":
    main()
