x = float(input("First number: "))
y = float(input("Second number: "))
operation: str = str(input("Your operation: "))

result = None

if operation in "+":
    result = x + y
    print("Result: ", result)
if operation in "-":
    result = x - y
    print("Result: ", result)
if operation in "*":
    result = x * y
    print("Result: ", result)
for operation in "/":
    if y == 0:
        print("На нуль ділити не можна")
        x2 = int(input("First number: "))
        y2 = int(input("Second number: "))
        operation2 = str(input("Your operation: "))
        result = x / y
        print("Result: ", result)
    break
