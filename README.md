# TO-DO-App-Django API's

Basic and simple API's around a To-Do application.

1. GET - 
    http://localhost:8000/      - endpoint to see all tasks.
    http://localhost:8000/?complete=False       - endpoint to see all uncompleted tasks.
    http://localhost:8000/?complete=True       - endpoint to see all completed tasks.
    
2. POST -
    http://localhost:8000/      - endpoint to create a new Task (required field 'title').
