# TO-DO-App-Django API's

Basic and simple API's around a To-Do application.

1. GET - 
    http://localhost:8000/      - endpoint to see all tasks.
    http://localhost:8000/task-detail/pk      - endpoint to see task with id=pk.
    http://localhost:8000/?complete=False       - endpoint to see all uncompleted tasks.
    http://localhost:8000/?complete=True       - endpoint to see all completed tasks.
    
2. POST -
    http://localhost:8000/      - endpoint to create a new Task (required field 'title').
    
3. PUT - 
    http://localhost:8000/task-detail/pk      - endpoint to update a Task.
    
4. DELETE - 
    http://localhost:8000/task-detail/pk      - endpoint to delete a Task.
