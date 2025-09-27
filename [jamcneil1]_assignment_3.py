#Step 1

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

#Step 2

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
