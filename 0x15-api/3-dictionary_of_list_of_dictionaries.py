#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the JSON format."""

import json
import requests
import sys


if __name__ == "__main__":
    json_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(json_url)
    employees = response.json()

    data_dict = {}

    for employee in employees:
        USER_ID = employee.get('id')
        username = employee.get('username')

        # Break the long URL into multiple lines
        todos_url = ('https://jsonplaceholder.typicode.com/users/{}/'
                     'todos').format(USER_ID)

        response = requests.get(todos_url)
        tasks = response.json()
        data_dict[USER_ID] = []

        for task in tasks:
            data_dict[USER_ID].append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data_dict, f)
