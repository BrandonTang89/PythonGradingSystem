from flask import Flask
from flask import render_template
from subprocess import check_output
from flask import request
import json

from python_grader_module import *
app = Flask(__name__)

use_docker = False

@app.route('/')
def hello_world():
    problems = (check_output("ls problems/", shell=True).decode("utf-8") ).split("\n")
    problems.pop()
    #print(problems)
    return render_template('main_page.html', problems=problems)

@app.route('/submit', methods=['POST'])
def submit():
    student_source_code = request.form['source_code']
    problem_name = request.form['problem_name']

    print("Problem: ", problem_name)
    print("Student Solution: ", student_source_code)

    (score, number_of_test_cases, percentage, outcome) = grade_solution(problem_name, student_source_code, use_docker)
    
    return (json.dumps({'status':'OK', "Problem":problem_name, "Score":score, "number_of_test_cases": number_of_test_cases, "percentage": percentage, "outcome": outcome}))

if __name__ == "__main__":
    use_docker = False
    print("Docker Sandboxing Disabled, Be Careful...")
    app.run(port='3000', host='0.0.0.0')
