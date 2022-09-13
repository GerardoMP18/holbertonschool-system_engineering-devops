#!/usr/bin/python3
""" script to export data in the JSON format all users"""

import json
import requests


if __name__ == "__main__":
    endpointUser = "https://jsonplaceholder.typicode.com/users"
    responseUser = requests.get(endpointUser).json()

    endpTodos = "https://jsonplaceholder.typicode.com/todos"
    responseTodos = requests.get(endpTodos)
    task = responseTodos.json()

    listdataID = {}
    for users in responseUser:
        newList = []
        for tasks in task:
            if tasks.get("userId") == users.get("id"):
                newdict = {}
                newdict['task'] = tasks.get("title")
                newdict['completed'] = tasks.get("completed")
                newdict['username'] = users.get("username")
                newList.append(newdict)
        listdataID[users.get("id")] = newList

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(listdataID, json_file)
