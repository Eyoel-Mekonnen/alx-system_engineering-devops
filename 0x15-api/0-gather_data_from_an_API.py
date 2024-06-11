#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    id_ = int(sys.argv[1])
    to_do_api = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id_)
    user_api = "https://jsonplaceholder.typicode.com/users"
    to_do_api_response = requests.get(to_do_api)
    user_api_response = requests.get(user_api)
    to_do = to_do_api_response.json()
    user = user_api_response.json()
    for value in user:
        if value["id"] == id_:
            employee_name = value["name"]
    number_of_completed = 0
    total_number_of_task = 0
    list_of_tasks_completed = []
    for value in to_do:
        if value["userId"] == id_ and value["completed"] == True:
            number_of_completed = number_of_completed + 1
            list_of_tasks_completed.append(value["title"])
        elif value["userId"] == id_ and value["completed"] == False:
            total_number_of_task = total_number_of_task + 1
    total_number_of_task = total_number_of_task + number_of_completed
    print("Employee {} is done with tasks({}/{}):".format(employee_name, number_of_completed, total_number_of_task))
    for tasks in list_of_tasks_completed:
        print("     {}".format(tasks))
