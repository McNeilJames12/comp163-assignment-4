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

  

