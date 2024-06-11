#!/usr/bin/python3
"""Fetches API and covert to API"""
import csv
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
            user_name = value["username"]
            user_id = id_
    list_ = []
    for value in to_do:
        csv_dict = {}
        if value["userId"] == id_:
            csv_dict["USER_ID"] = id_
            csv_dict["USERNAME"] = user_name
            csv_dict["TASK_COMPLETED_STATUS"] = value["completed"]
            csv_dict["TASK_TITLE"] = value["title"]
            list_.append(csv_dict)

    fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    file_name = "{}.csv".format(id_)
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields,
                                quoting=csv.QUOTE_ALL)
        writer.writerows(list_)
