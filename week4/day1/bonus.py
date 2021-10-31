
# Write a code that receives 3 inputs and combines them:
# A number input (integer, float etc.)
# A number input (integer, float etc.)
# A string, describing an operator (“add”, “multiply”, “divide”)
# If the first two inputs are equal -> print number1 with the power of number2.
# Otherwise, perform the 3rd input’s operator on number1 with number2 and print the result.
# If the input from the user isn’t correct -> print an error message.

while True:
    try:
        num_one = int(input('Enter a number'))
        num_two = int(input('Enter a number'))
        operator = input('Choose an operator: +, * or /')
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if num_one == num_two: 
        x = num_one**num_two
        print(x)
    else:
        if operator == '+':
            print(num_one+num_two)
        elif operator == '*':
            print(num_two*num_one)
        elif operator == '/':
            print(num_one/num_two)
        
            