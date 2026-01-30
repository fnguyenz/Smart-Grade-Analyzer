"""
Smart Grade Analyzer Project
This is my first project as a Master of Infotech!
This will be used to calculate a students average grade given their scores in a course.
User will be able to input scores between 0-100, and can let the code know when they are done to begin calculations.
"""
# import modules required (eg. regex)
import re

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

# greet user, ask for the number of courses they'd like to calculate for (or ask them to begin listing their grades)



# check for any invalid characters using regex, tell them to re-state that grade properly


# once user states they are done listing, calculate the average using the number of courses they inputted into the system


# obtain users name and then call upon a function to begin
name = input("Hey user! Before we start calculating, what is your name?\n\n").strip().capitalize()
print(f"Thanks {name}, let's begin now.")

