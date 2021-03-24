
# '''
a = float(input())
sign = input()[0]
b = float(input())
c = 0
if sign == "+":
    c = a + b
elif sign == "-":
    c = a - b
elif sign == "*":
    c = a * b
elif sign == "/":
    c = a / b
elif sign == "%":
    c = a % b
print(f"={c}")
# '''
# print(f"= {eval(input())}")