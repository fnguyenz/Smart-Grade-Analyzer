"""
Smart Grade Analyzer Project
This is my first project as a Master of Infotech!
This will be used to calculate a students average grade given their scores in a course.
User will be able to input scores between 0-100, and can let the code know when they are done to begin calculations.
"""

# define variables
courses = []
done = False
num = len(courses) # collect the number of courses through the number of grades inputted.

# # state letter grades based on numerical percentages
# Aye = range(86, 101)
# Bee = range(73, 86)
# Cplus = range(67, 73)
# Cee = range(60, 67)
# Cminus = range(50, 60)
# Eff = range(0, 50)

# once user states they are done listing, calculate the average using the number of courses they inputted into the system
def calculation():

    # collect each number within the list of courses, and add them all together
    totalsum = sum(courses)
    avg = round(totalsum/len(courses))

    # with the average, check which letter grade the average corresponds with
    if avg in range(86, 101):
        lettergrade = "A"
    elif avg in range(73, 86):
        lettergrade = "B"
    elif avg in range(67, 73):
        lettergrade = "C+"
    elif avg in range (60, 67):
        lettergrade = "C"
    elif avg in range(50, 60):
        lettergrade = "C-"
    else:
        lettergrade = "F"
    # state the highest and lowest grade the user received

    # print the results; average, highest/lowest, and letter grade
    print(f"Out of your {len(courses)} grades: your grade average is {avg}, which is a {lettergrade}")


# begin the calculating, allow for user to begin inputting values,
def collect(done):
    print("Please input one grade at a time and using your grade percentage! (e.g. 96, 75)\n\nInput DONE to calculate.")
    
    # loop that goes on while the users grade input is still ongoing.
    while not done:

        # let user know how many courses theyve inputted so far.
        print(f"Number of courses inputted: {len(courses)}")
        userinput = input("Course Grade:   ").strip() # variable of each grade

        # if there are 2 or more inputs and user states they are done, move on to the next step.
        # break loop when user states they are done
        if userinput == "done":
            if len(courses) >= 2: 
                done = True
                calculation()
                break
            
            # if there is not enough courses, continue the loop
            else:
                print("\nPlease input at least 2 grades in order to calculate.\n")
                continue
        # before converting grade into integer, determine if it is valid (and if user is not done.)
        elif not userinput.isdigit():
            print("\nThis is not a valid grade! please input a proper grade percentage.\n")
            continue
        else:
            grade = int(userinput)

        # if grade goes beyond 100, or below 0, it is invalid.
        if grade <= 0 or grade > 100: 
            print("That is not a valid grade, please input a grade percentage!")
            continue
        else:
            courses.append(grade) # save each input into the list
            print(courses) # see which grades you have inputted so far.
            continue

    

# obtain users name and then call upon a function to begin
name = input("Hey user! Before we start calculating, what is your name?\n\n").strip().capitalize()
print(f"Thanks {name}, let's begin now.\n\n")

collect(False)
