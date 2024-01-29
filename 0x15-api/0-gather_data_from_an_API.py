#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her Todo list progress."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_ID = sys.argv[1]
    jsonplaceholder = 'https://jsonplaceholder.typicode.com/users'
    url = f'{jsonplaceholder}/{employee_ID}'

    response = requests.get(url)

    if response.status_code == 200:
        employee_name = response.json().get('name')
        Todourl = f'{url}/todos'
        res = requests.get(Todourl)
        tasks = res.json()

        done_tasks = [task for task in tasks if task.get('completed')]

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, len(done_tasks), len(tasks)))
        for task in done_tasks:
            print("\t{}".format(task.get('title')))
    else:
        print(f"Error: Status code: {response.status_code}")
