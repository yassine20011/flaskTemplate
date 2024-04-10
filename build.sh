#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python app.py & sleep 5
        
status=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/)
if [ $status -eq 200 ]; then
  echo "Flask application is running successfully."
else
  echo "Flask application is not running or returned status $status."
  exit 1 
fi

exit 0