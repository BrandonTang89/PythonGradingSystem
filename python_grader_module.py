from subprocess import check_output
from subprocess import TimeoutExpired
from random import randint

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

def grade_solution(target_problem, student_solution ):
    student_base_name = "student_" + str(randint(0,1000)) + ".py"
    student_file_name = "student_code/" + student_base_name# Random int to prevent overwrite of other executing files
    print("Saving Solution to:", student_file_name)
    target_problem =  "problems/" + target_problem
    
    

    # Write Student Solution to File
    f =  open(student_file_name, 'w')
    f.write(student_solution)
    f.close()
        
    # Read Meta Data about Problem
    solution_file_name = target_problem + "/solution.py"
    with open(target_problem + "/testcases.cfg") as f:
        number_of_test_cases = int(f.readline())
        time_limit = int(f.readline())

    score = 0
    state = "Normal"
    for i in range(1, number_of_test_cases+1):
        correct_out = str(check_output("cat " + target_problem + "/" +  str(i) +".in | python3 " + solution_file_name, shell=True))
        print("Test Case " + str(i))
        print(" Correct Output: " +  correct_out)

        try:
            #student_out = str(check_output("cat " + target_problem + "/" +  str(i) +".in | python3 " + student_file_name, timeout=time_limit, shell=True))
            # Docker Containerisation
            student_out = str(check_output("cat " + target_problem + "/" +  str(i) + '.in  | docker run -i --rm -v "$(pwd)/student_code":/student -w /student python:3 python3 ' + student_base_name,shell=True))
        except TimeoutExpired:
            print(" Solution Time Limit Exceeded [TLE]")
            
            if state == "Normal":
                state = "TLE"

            elif state == "RTE":
                state += " & TLE"
            student_out = ""
            
        except Exception as e:
            print(" Solution Runtime Error       [RTE]")
            print(" Details: " + str(e))

            if state == "Normal":
                state = "RTE"

            elif state == "TLE":
                state += " & RTE"
            
            student_out = ""
            
        print(" Student Output: " +  student_out)

        if student_out == correct_out:
            print("Correct")
            score+= 1
        else:
            print("Incorrect")
        
        # Test the student solution against the test case, with ideal result being the solution.py file

    percentage = score*100/number_of_test_cases
    if score != number_of_test_cases and state=="Normal":
        state = "WA"
        
    print("Score: " + str(score) + " / " + str(number_of_test_cases) + ", Percentage: " + str(percentage) + "% Status: " + state)
    check_output("rm " + student_file_name, shell=True)
    return (score, number_of_test_cases, percentage, state)

#grade_solution("bracket", student_solution)
