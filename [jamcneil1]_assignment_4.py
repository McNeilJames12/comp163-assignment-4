# Step 1

student_name = "James McNeil"
current_gpa = 4.0
study_hours = 22
social_points = 99
stress_level = 87


print(f"Welcome {student_name} to the Student Life Tracker!")
print(f"Your current GPA is a {current_gpa}!")
print(f"Your study hours are at {study_hours}!")
print(f"Your social points are at {social_points} points!")
print(f"Your stress level is at {stress_level}.")

# Step 2

light_course = "Baby food, you got it easy (12 credits)"
standard_course = "Make sure you focus (15 credits)"
heavy_course = "Lock in lil twin, library is 24 hours (18 credits)"


print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
choice = input("Your choice: ")

if choice == "A":
  print(f"Course Option Selected: {light_course}")
elif choice == "B":
    print(f"Course Option Selected: {standard_course}")
elif choice == "C":
    print(f"Course Option Selected: {heavy_course}")
else:
  print("ERROR! Enter the correct letter that is equal to your perfered course option!")

# Step 3

study = ["Programming", "Math", "English", "History"]
print("Which class would you like to study:")
study_choice = input("Choice selected: ")

if study_choice in study:
    if study_choice == "Programming":
        current_gpa += 0.4
        social_points -= 15
        print("You chose a pretty hard subject twin, looks like you're not going outside lol")
    elif study_choice == "Math":
        current_gpa += 0.3
        social_points -= 5
        print("Are you a nerd or something?")
    elif study_choice == "English" and current_gpa >= 3.0:
        social_points += 10
        print("'Perfectly balanced, as all things should be' - Thanos")
    elif study_choice == "History" or (study_choice == "English" and current_gpa < 3.0):
        current_gpa += 0.1
        social_points += 7
        print("I'm proud of you, keep up the good work!")
        
    else:
        study_choice not in study, print("Invalid")

# Step 4

final_goal = input("What is your ultimate goal? ")

if type(final_goal) is str:
    print(f"Goal '{final_goal}'.")
    if current_gpa > 4.2:
        print("Twin you looking like you're ready for Harvard, I'm proud of you!")
    elif current_gpa >= 3.8:
        print("Okay then, you looking like a big nerd. Keep up the good work!")
        if social_points > 90 and stress_level < 85:
            print("You were locked in with your grades while keeping having fun and still keeping your mental health in check. The perfect semester!")
        else:
            print("Great grades but remember that you matter more twin. Go rest!")
    else:
        print("Your final GPA is below what we wanted. Next semester, focus on raising those study hours and lock in! Remember, the library is 24 hours!")

elif type(final_goal) is not str:
    print("Identity check: Goal input must be text.")

print(f"Final GPA: {current_gpa:.2f}")
print(f"Total Study Hours: {study_hours} hours")
print(f"Total Social Points: {social_points} points")
print(f"Final Stress Level: {stress_level}")
print(f"Had fun with you twin, see you next time!")
