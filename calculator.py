import math_utils

operations = {"A" : math_utils.add,
              "S" : math_utils.subtract,
              "M" : math_utils.multiply,
              "D" : math_utils.divide,
              "P" : math_utils.power,
              "MOD" : math_utils.mod
              }


def main():
    first = int(input("please enter the first value: "))
    second = int(input("please enter the second value: "))
    op = input("A for add\nS for subtract\nM for multiply\nD for divide\nP for power\nMOD for mod: ")

    if op not in operations:
        print("invalid input")
        return
    print("the answer: ", operations[op](first, second))



if __name__ == "__main__":
    main()
