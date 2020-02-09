from subprocess import check_output

target_problem =  "problems/" + "bracket"
student_file_name = "student.py"
student_solution = '''

sequence = input()
valid= True
counter = 0
for i in sequence:
    if i == '(':
        counter+=1
    else:
        counter-=1
        if counter < 0:
            valid = False
            break
if counter > 0:
    valid = False
    
if valid:
    print("Valid")
else:
    print("Invalid")
'''

# Write Student Solution to File
f =  open(student_file_name, 'w')
f.write(student_solution)
f.close()
    
# Read Meta Data about Problem
solution_file_name = target_problem + "/solution.py"
with open(target_problem + "/testcases.cfg") as f:
    number_of_test_cases = int(f.read())

score = 0
for i in range(1, number_of_test_cases+1):
    correct_out = str(check_output("cat " + target_problem + "/" +  str(i) +".in | python3 " + solution_file_name, shell=True))
    print("Test Case " + str(i))
    print(" Correct Output: " +  correct_out)

    student_out = str(check_output("cat " + target_problem + "/" +  str(i) +".in | python3 " + student_file_name, shell=True))
    print(" Student Output: " +  student_out)

    if student_out == correct_out:
        print("Correct")
        score+= 1
    else:
        print("Incorrect")
    
    # Test the student solution against the test case, with ideal result being the solution.py file
    

print("Score: " + str(score) + " / " + str(number_of_test_cases) + ", Percentage: " + str(score*100/number_of_test_cases) + "%")
