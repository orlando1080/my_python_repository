Num1 = None
Op = None
Num2 = None

print('Please enter your first number:')
Num1 = int(input())
print('Please enter your operator:')
print('Please enter your second number:')
Num2 = int(input())
if Op == '+':
    print(Num1 + Num2)
elif Op == '-':
    print(Num1 - Num2)
elif Op == '/':
    print(Num1 / Num2)
elif Op == '*':
    print(Num1*Num2)