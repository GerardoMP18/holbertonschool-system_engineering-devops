#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress."""


import requests
import sys


if __name__ == "__main__":
    endpointUser = "https://jsonplaceholder.typicode.com/users/{}".format(
            sys.argv[1])

    responseUser = requests.get(endpointUser)
    EMPLOYEE_NAME = responseUser.json().get("name")

    endpTodos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            sys.argv[1])

    responseTodos = requests.get(endpTodos)
    task = responseTodos.json()
    TOTAL_NUMBER_OF_TASKS = len(task)

    NUMBER_OF_DONE_TASKS = 0
    for tasks in task:
        if tasks.get("completed") is True:
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUMBER_OF_TASKS
                                                          ))

    for tasks in task:
        if tasks.get("completed") is True:
            TASK_TITLE = tasks.get("title")
            print("\t {}".format(TASK_TITLE))
