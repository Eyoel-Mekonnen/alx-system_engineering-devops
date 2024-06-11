#!/usr/bin/python3
""" Fetch API and store it in JSON for all"""
import json
import requests
import sys

if __name__ == "__main__":
    to_do_ = "https://jsonplaceholder.typicode.com/todos"
    user_api = "https://jsonplaceholder.typicode.com/users"
    to_do_api_response = requests.get(to_do_)
    user_api_response = requests.get(user_api)
    to_do = to_do_api_response.json()
    user = user_api_response.json()
    dict_list = {}
    for value in user:
        list_ = []
        for value_todo in to_do:
            csv_dict = {}
            if value["id"] == value_todo["userId"]:
                csv_dict["username"] = value["username"]
                csv_dict["task"] = value_todo["title"]
                csv_dict["completed"] = value_todo["completed"]
                list_.append(csv_dict)
        id_final = str(value["id"])
        dict_list["{}".format(id_final)] = list_
    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as json_file:
        json_file.write(json.dumps(dict_list))
