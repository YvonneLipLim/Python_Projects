print("Welcome to the PSLE Score Generator")
print("------------------------------------------------------------------------------")
print("Instructions:")
print("1. Enter your marks for each subject.")
print("2. The program will calculate your PSLE score and placement stream.")
print("------------------------------------------------------------------------------")

def valid_entry(prompt, min_value = 0, max_value = 100):
    """Get user input a valid integer within 0 to 100"""
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Invalid input. Enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Enter a valid integer.")

def valid_yes_no(prompt):
    """Get user input a Yes/No question"""
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "no", "y", "n"]:
            return response
        print("Invalid input. Enter Yes or No.")

def student_raw_mark(marks):
    """Map raw score to PSLE Achievement Levels (ALs)"""
    if marks >= 90:
        return "1"
    elif 85 <= marks <= 89:
        return "2"
    elif 80 <= marks <= 84:
        return "3"
    elif 75 <= marks <= 79:
        return "4"
    elif 65 <= marks <= 74:
        return "5"
    elif 45 <= marks <= 64:
        return "6"
    elif 20 <= marks <= 44:
        return "7"
    else:
        return "8"

def student_higher_mt(grade):
    """Map raw score of Higher Mother Tongue Language to grade"""
    if grade >= 80:
        return "Distinction"
    elif 65 <= grade <= 79:
        return "Merit"
    elif 50 <= grade <= 64:
        return "Pass"
    else:
        return "Fail"

def student_placement(score):
    """Define student placement stream accordingly to PSLE score"""
    if score <= 20:
        return "Express"
    elif score <= 22:
        return "Express / Normal (Academic)"
    elif score <= 24:
        return "Normal (Academic)"
    elif score == 25:
        return "Normal (Academic) / Normal (Technical)"
    elif score <= 30:       
        return "Normal (Technical) - above AL7 in English and Math"
    else:
        return "Normal (Technical)"

def print_results(subject, marks, al):
    """Print subject-wise results."""
    print(f" {subject:23} | {marks:4} | {al}")
    
#Get marks for each subject
english_marks = valid_entry("\nEnter your English marks: ")
mother_tongue_marks = valid_entry("Enter your Mother Tongue marks: ")
math_marks = valid_entry("Enter your Mathematics marks: ")
science_marks = valid_entry("Enter your Science marks: ")
took_higher_mt = valid_yes_no("Did you take Higher Mother Tongue Language? [Yes/No]: ")
if took_higher_mt in ["yes", "y"]:
    higher_mt_marks = valid_entry("Enter your Higher Mother Tongue marks: ")
else:
    higher_mt_marks = None

#Get ALs for each subject 
english_al = student_raw_mark(english_marks)
mother_tongue_al = student_raw_mark(mother_tongue_marks)
math_al = student_raw_mark(math_marks)
science_al = student_raw_mark(science_marks)

#For students who took higher mother tongue
if took_higher_mt in ["yes", "y"]:
    higher_mt = student_higher_mt(higher_mt_marks)
else:
    higher_mt = "Not Taken"
    
#Calculate the total PSLE score and define a variable for the placement steam
psle_score = 0
for al in [english_al, mother_tongue_al, math_al, science_al]:
    psle_score += int(al) if al != "" else 7
placement = student_placement(psle_score)

#Print PSLE results
print("\nPSLE Results")
print("------------------------------------------------------------------------------")
print(" | Subject               | Mark | Achievement Level")
print("------------------------------------------------------------------------------")
print_results(f"| English", english_marks, english_al)
print_results(f"| Mother Tongue", mother_tongue_marks, mother_tongue_al)
print_results(f"| Mathematics", math_marks, math_al)
print_results(f"| Science", science_marks, science_al)
if took_higher_mt in ["yes", "y"]:
    print(f" | Higher Mother Tongue: |", higher_mt)
print("------------------------------------------------------------------------------")
print(f"\n | PSLE Score                          : {psle_score}")
print(f" | Secondary School Course Eligible For: {placement}")
print("------------------------------------------------------------------------------")
