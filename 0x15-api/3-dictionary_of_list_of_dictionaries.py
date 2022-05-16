#!/usr/bin/python3
"""Get todos from user."""
import json
import requests

if __name__ == "__main__":

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    users_dict = {}

    for user in users:
        todos = requests.get("""
                https://jsonplaceholder.typicode.com/users/{}/todos
                """.format(str(user.get('id')))).json()
        users_dict[str(user.get('id'))] = []
        for todo in todos:
            td = {"task": todo.get('title'),
                  "completed": todo.get('completed'),
                  "username": user.get('username')}
            users_dict[str(user.get('id'))].append(td)

    with open("todo_all_employees.json", 'w') as f:
        json.dump(users_dict, f)
