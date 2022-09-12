#!/usr/bin/python3
""" script to export data in the CSV format """

import csv
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

    with open('{}.csv'.format(sys.argv[1]), 'w', encoding='utf-8') as file_csv:
        writer = csv.writer(file_csv, quoting=csv.QUOTE_ALL)
        for tasks in task:
            USER_ID = sys.argv[1]
            TASK_COMPLETED_STATUS = tasks.get('completed')
            TASK_TITLE = tasks.get('title')
            writer.writerow([USER_ID, USERNAME,
                             TASK_COMPLETED_STATUS, TASK_TITLE])
