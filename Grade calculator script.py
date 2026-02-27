#Grade calculator script that takes in a percentage and outputs the corresponding letter grade.
#define a function called calculate_grade that takes a percentage as input and returns the corresponding letter grade based on the following scale:
#90% and above: A
#80% to 89%: B
#70% to 79%: C
#60% to 69%: D
#below 60%: F   
#prompt the user to enter their percentage grade and call the calculate_grade function with the user's input. Finally, print the letter grade to the user.'
    # The function should use if-elif-else statements to determine the correct letter grade based on the input percentage. 
    # The program should also handle invalid inputs (e.g., non-numeric values or percentages outside the 0-100 range) gracefully by displaying an appropriate error message.

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'



def main():
    try:
        percentage = float(input("Enter your percentage grade: "))
        if 0 <= percentage <= 100:
            letter_grade = calculate_grade(percentage)
            print(f"Your letter grade is: {letter_grade}")
        else:
            print("Please enter a valid percentage between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the percentage.")

if __name__ == "__main__":
    main()
