dict = {'Ishant': 99, 'Prashant': 87, 'Sujata': 96}
a = input("Enter the student's name: ")
if a in dict:
    print(f"{a}'s marks: {dict[a]}")
else:
    print("Student not found")