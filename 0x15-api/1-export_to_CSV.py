#!/usr/bin/python3
"""Get todos from user."""
import requests
from sys import argv

if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
    todos = todos.json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    user = user.json()
    with open(str(user.get('id'))+".csv", 'w') as f:
        for todo in todos:
            f.write('"{}","{}","{}","{}"\n'
                    .format(user.get('id'), user.get('username'),
                            todo.get('completed'), todo.get('title')))
