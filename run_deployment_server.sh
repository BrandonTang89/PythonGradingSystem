sudo rm -r student_code
mkdir student_code
gunicorn3 --bind 0.0.0.0:5000 web_server:app