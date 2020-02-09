# PythonGradingSystem
A Mini Online Judge Server to help grade short programming assignments in python

This is a simplified online grading system to evaluate programming assignments written in python 3+. It is scalable with new problems being able to be added and has an integrated online portal for submission of source code (in plain text).

## Dependencies
Install the required dependencies of 
1. python 3.6+
2. flask (python webserver library)
3. Gunicorn3 (http server)
4. docker (containerisation software) 

To install python 3.6+, go to [the python home page](https://python.org) and follow the instructions.

To install flask
<pre>
pip3 install flask
</pre>
 
To install gunicorn3
<pre>
sudo apt-get update
sudo apt-get install gunicorn3
</pre>

To install docker, follow [the instruction guide here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04). **Important: Follow the steps to run docker without sudo.**

# Usage
## Running the Server
Clone the repository, then open a terminal in the root folder of the repository.

Start the server with:
<pre>
chmod +x run_deployment_server.sh
./run_deployment_server.sh
</pre>
*The sudo prompt is for deleting the cached student submissions folder that may be write protected by docker*

## Adding New Problems
Each problem in the judge is a separate directory in the "problems" folder where the problem name is the directory name.

Each problem has 1 or more test cases (.in files) and an "intended solution" python file which will be used to generate the "correct" answers for each  test case. The files are organised as follows.
<pre>
Structure of Problems

problems
	|
	--- problem_name
			|
			--- testcases.cfg
			|
			--- solution.py
			|
			--- i.in [for i in [1,number of test cases]]

testcases.cfg contains 2 lines.
	1. The number of testcases
	2. The time limit for execution (in seconds [int])

solution.py is the intended solution
	Used to generate "correct output" for each test case on the fly
	Should read from standard input

i.in is the ith input file.
	Student's solution should read from standard input
</pre>


# Design and Implementation Details
## Grading System
The grader accepts student solutions from the font-end web portal via an AJAX post request, this solution is then temporarily saved in a file with the name "student_xxx.py" where xxx is random number in the range [1, 1000] within the student_code directory. 

The grader then iterates through each testcase in the problem that is being attempted. The solution.py file is used to determine the correct output and this is compared to the output of the student_xxx. The number of testcases correct is returned in the post request response to be displayed to the user.

In the event of the student code taking longer than the allowed time to execute, a "time limit exceeded (TLE)" response is given. If the student's code encounters an exception, a "runtime error (RTE)" response is returned. Else, either a "wrong answer (WA)" or "all correct (AC)" response is given.

## Untrusted Code Execution Details
To prevent execution of malicious code that could destory the host machine, this project uses docker conntainers to sandbox the execution of the student scripts. Whenver a student script is executed, a docker python:3 container is created which has access to the "student_code" directory via a volume mount. The student script is then executed within the docker container.

Thus, the only directory that can be affected by the student code is the "student_code" directory which will be emptied upon restarting the server.

Furthermore, infinite loops and resource exhaustion attacks are mitigated via the time limit on execution time. That being said, this is dependant on the time limit set on each individual problem. Therefore, it is advised to set a short time limit that will only allow the intended algorithm implementation to succeed.

Note: Using Docker results in about 0.5 seconds of overhead per testcase, I'm still working on a get-around.

