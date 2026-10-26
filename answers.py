#Question 1
x = 0
y = 0
x += 3;
y *= 2;
result = x / y;
print(result);

#Question 2
a = float(input("Enter a value for a: "));
b = float(input("Enter a value for b: "));
c = float(input("Enter a value for c: "));
c1 = (a > b);
c2 = (b % 2 == 0);
c3 = (c <= a);
final_condition = False;
if(c1):
    final_condition = True;
elif(c2 and c3):
    final_condition = True;
else:
    final_condition = False;

#Question 3
gradescore = int(input("Enter your test score (0-100): "));
if (gradescore >= 90):
    grade = "A";
elif (gradescore >= 80):
    grade = "B";
elif (gradescore >= 70):
    grade = "C";
elif (gradescore >= 60):
    grade = "D";
else:
    grade = "F";

print("Your grade is " + grade);

#Question 4
num1 = float(input("Enter your first number: "));
num2 = float(input("Enter your second number: "));
symbol = input("Enter the operation (+, -, *, /): ");
if (symbol == "+"):
    result = num1 + num2;
elif (symbol == "-"):
    result = num1 - num2;
elif (symbol == "*"):
    result = num1 * num2;
elif (symbol == "/"):
    if (num2 != 0):
        result = num1 / num2;
    else:
        result = "Error: Division by zero is not allowed.";
print("The result is: " + str(result));