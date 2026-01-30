"""
Smart Grade Analyzer Project
This is my first project as a Master of Infotech!
This will be used to calculate a students average grade given their scores in a course.
User will be able to input scores between 0-100, and can let the code know when they are done to begin calculations.
"""
# import modules required (eg. regex)
import re
import math

# define variables
courses = []
done = False
num = len(courses) # collect the number of courses through the number of grades inputted.

# state letter grades based on numerical percentages
A = list(range(86, 101))
B = list(range(73, 86))
Cplus = list(range(67, 73))
C = list(range(60, 67))
Cminus = list(range(50, 60))
F = list(range(0, 50))

# begin the calculating, allow for user to begin inputting values,
def collect():
    print("Please input one grade at a time and using your grade percentage! (e.g. 96, 75)\n\nWhen you are done, type DONE")
    while not done:
        for loop in range():
            grade = int(input("Course Grade:   ").strip().isnumeric())
            courses.append(grade) # save each input into the list

            if num <= 2:
                input("Anything else? [Y / N]\n").strip().isalpha()
                if "y": 
                    done = True
                if "n":
                    done = False
                else:
                    print("Not a valid input, please indicate Y or N!")
                    return
            break
        break
    while done:
        print("not done yet!")

# check for any invalid characters using regex, tell them to re-state that grade properly


# once user states they are done listing, calculate the average using the number of courses they inputted into the system

# obtain users name and then call upon a function to begin
name = input("Hey user! Before we start calculating, what is your name?\n\n").strip().capitalize()
print(f"Thanks {name}, let's begin now.")

collect()
