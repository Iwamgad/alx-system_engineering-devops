#!/usr/bin/python3
"""This python script returns to-do list information for a given
employee ID in the CSV format
"""

import csv
import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userId)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.csv".format(userId), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [userId, username, t.get("completed"), t.get("title")]
        ) for t in todos]
