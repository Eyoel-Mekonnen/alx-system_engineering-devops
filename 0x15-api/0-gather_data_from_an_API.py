#!/usr/bin/python3

""" Fetches users and todo from the API"""
import requests
import sys

if __name__ == "__main__":
    id_ = int(sys.argv[1])
    to_do_ = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id_)
    user_api = "https://jsonplaceholder.typicode.com/users"
    to_do_api_response = requests.get(to_do_)
    user_api_response = requests.get(user_api)
    to_do = to_do_api_response.json()
    user = user_api_response.json()
    for value in user:
        if value["id"] == id_:
            employee_name = value["name"]
    number_of_completed = 0
    total_number_task = 0
    list_of_tasks_completed = []
    for value in to_do:
        if value["userId"] == id_ and value["completed"] is True:
            number_of_completed = number_of_completed + 1
            list_of_tasks_completed.append(value["title"])
        elif value["userId"] == id_ and value["completed"] is False:
            total_number_task = total_number_task + 1
    total_number_task = total_number_task + number_of_completed
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          number_of_completed,
                                                          total_number_task))
    for tasks in list_of_tasks_completed:
        print("\t {}".format(tasks))
