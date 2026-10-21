"""Dictionary basics: create, access, update, delete and iterate."""

# Create a dictionary: keys on the left, values on the right
student = {
    "name": "Kavya",
    "age": 22,
    "course": "Python",
    "marks": 88.5,
}
print("1. Created dictionary:")
print(student)
print()

# Access values by key, and safely with get()
print("2. Accessing values:")
print("Name:", student["name"])
print("Marks:", student["marks"])
print("Grade (missing key):", student.get("grade", "Not available"))
print()

# Update an existing value and add a new key
student["marks"] = 91.0
student["grade"] = "A"
print("3. After updating marks and adding grade:")
print(student)
print()

# Delete a key with pop(), which also returns the removed value
removed = student.pop("age")
print(f"4. Removed 'age' ({removed}). Dictionary now:")
print(student)
print()

# Check if a key exists with 'in'
print("5. Is 'course' a key?", "course" in student)
print("   Is 'age' a key?", "age" in student)
print()

# Iterate through keys, values and key-value pairs
print("6. Iterating:")
for key in student:
    print("Key:", key)
for value in student.values():
    print("Value:", value)
for key, value in student.items():
    print(f"{key} -> {value}")
print()

# A dictionary of dictionaries: several students, looked up by ID
students = {
    "S1": {"name": "Asha", "marks": 82},
    "S2": {"name": "Ravi", "marks": 67},
    "S3": {"name": "Meera", "marks": 91},
}
print("7. Nested dictionary:")
total = 0
for student_id, record in students.items():
    print(f"{student_id}: {record['name']} scored {record['marks']}")
    total += record["marks"]
print(f"Average marks: {total / len(students):.1f}")