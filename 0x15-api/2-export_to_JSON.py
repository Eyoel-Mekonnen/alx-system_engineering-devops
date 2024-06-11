#!/usr/bin/python3
"""Fetch API and store it in JSON"""
import json
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
            username = value["username"]
            user_id = id_
    list_ = []
    for value in to_do:
        csv_dict = {}
        if value["userId"] == id_:
            csv_dict["task"] = value["title"]
            csv_dict["completed"] = value["completed"]
            csv_dict["username"] = username
            list_.append(csv_dict)

    dict_list = {}
    id_final = str(id_)
    dict_list["{}".format(id_final)] = list_
    file_name = "{}.json".format(id_)
    with open(file_name, 'w') as jsonfile:
        jsonfile.write(json.dumps(dict_list))
