Get two integers x and y from the user and write a program to relate 2 integers as equal
to, less than or greater than.
Input format:
Input consist of 2 integers
The first input corresponds to the first number.(a)
The second input corresponds to the second number.(b)
Output format:
If the first number is equal to the second number, print "x and y are equal". Otherwise, print
"x greater than y" or "x less than y"
Sample Input:
6
8
Sample Output:
6 less than 8


x = int(input("Enter the first integer (x): "))
y = int(input("Enter the second integer (y): "))
if x == y:
    print("x and y are equal")
elif x > y:
    print("x greater than y")
else:
    print("x less than y")
