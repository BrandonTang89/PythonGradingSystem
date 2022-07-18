sudo rm -r student_code
mkdir student_code
while true
do
	export FLASK_APP=web_server.py
	export FLASK_ENV=development
	flask run
	sleep 1
done
