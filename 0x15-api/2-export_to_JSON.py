#!/usr/bin/python3
"""Get todos from user."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
    todos = todos.json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    user = user.json()
    user_dict = {str(user.get('id')): []}
    for todo in todos:
        td = {"task": todo.get('title'),
              "completed": str(todo.get('completed')),
              "username": user.get('username')}
        try:
            user_dict.get(str(user.get('id'))).append(td)
        except Exception:
            pass

    with open(str(user.get('id'))+".json", 'w') as f:
        json.dump(user_dict, f)
