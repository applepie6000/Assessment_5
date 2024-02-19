def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y

print("What do you want to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")
# print("5. Exit")

while True:
    choice = input("Enter your choice:1/2/3/4: ")
    if choice in ('1','2','3','4',):
        try:
            value_1 = float(input("Enter the first value"))
            value_2 = float(input("Enter the second value"))
        except ValueError:
            print("Invalid. Please try again.")


            if choice == '1':
                print(add(value_1,value_2))
            elif choice == '2':
                print(substract(value_1, value_2))
            elif choice=='3':
                print(multiply(value_1, value_2))
            elif choice=='4':
                print(division(value_1, value_2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")





























