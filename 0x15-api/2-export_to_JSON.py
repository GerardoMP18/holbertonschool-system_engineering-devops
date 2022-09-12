#!/usr/bin/python3
""" script to export data in the JSON format """

import json
import requests
import sys


if __name__ == "__main__":
    endpointUser = "https://jsonplaceholder.typicode.com/users/{}".format(
            sys.argv[1])

    responseUser = requests.get(endpointUser)
    USERNAME = responseUser.json().get("username")

    endpTodos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            sys.argv[1])

    responseTodos = requests.get(endpTodos)
    task = responseTodos.json()

    newList = []
    for tasks in task:
        newdict = {}
        newdict['task'] = tasks.get("title")
        newdict['completed'] = tasks.get("completed")
        newdict['username'] = USERNAME
        newList.append(newdict)

    listdataID = {sys.argv[1]: newList}

    with open("{}.json".format(sys.argv[1]), "w") as json_file:
        json.dump(listdataID, json_file)
