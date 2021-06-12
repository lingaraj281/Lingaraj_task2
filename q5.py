print("Enter 1st number")
num1 = int(input())

print("Enter 2nd number")
num2 = int(input())

print("Enter the operand")
operand = str(input())


add = num1 + num2
substract = num1 - num2
multiply = num1 * num2
div = num1 / num2
mod = num1 % num2

floating_num = "The answer is {:.2f}"

for x in operand:
    if x == "+":
        print(floating_num.format(add))
    elif x == "-":
        print(floating_num.format(substract))
    elif x == "*":
        print(floating_num.format(multiply))
    elif x == "/":
        print(floating_num.format(div))
    elif x == "%":
        print(floating_num.format(mod))
    else:
        print("Not a valid operation")