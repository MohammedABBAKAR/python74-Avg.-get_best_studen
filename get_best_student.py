# Get Student with Best Test Avg.

# Given a dictionary with students and the grades that they made on the tests that they took, determine which student has the best Test Average. The key will be the student's name and the value will be a list of their grades. You will only have to return the student's name. You do not need to return their Test Average.
# Examples

# get_best_student({
#   "John": [100, 90, 80],
#   "Bob": [100, 70, 80]
# }) ➞ "John"

# # John's avg = 90
# # Bob's avg = 83.33

# get_best_student({
#   "Susan": [67, 84, 75, 63],
#   "Mike": [87, 98, 64, 71],
#   "Jim": [90, 58, 73, 86]
# }) ➞ "Mike"

# Notes

# All students in a dictionary will have the same amount of test scores. So no student will have taken more tests than another.








def get_best_student(students):
    best_student = ""
    highest_avg = 0.0
    
    for student, scores in students.items():
        avg_score = sum(scores) / len(scores)
        if avg_score > highest_avg:
            highest_avg = avg_score
            best_student = student
    
    return best_student

# Test cases
print(get_best_student({
  "John": [100, 90, 80],
  "Bob": [100, 70, 80]
}))  # Output: "John"

print(get_best_student({
  "Susan": [67, 84, 75, 63],
  "Mike": [87, 98, 64, 71],
  "Jim": [90, 58, 73, 86]
}))  # Output: "Mike"







def get_best_student(students):
    # Calculate the average for each student and return the student with the highest average
    return max(students, key=lambda student: sum(students[student]) / len(students[student]))

# Test cases
test_case1 = {
    "John": [100, 90, 80],
    "Bob": [100, 70, 80]
}

test_case2 = {
    "Susan": [67, 84, 75, 63],
    "Mike": [87, 98, 64, 71],
    "Jim": [90, 58, 73, 86]
}

# Results
result1 = get_best_student(test_case1)  # Expected: "John"
result2 = get_best_student(test_case2)  # Expected: "Mike"

result1, result2
