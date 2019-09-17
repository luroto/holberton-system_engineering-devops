#!/usr/bin/python3
""" This script gets info from an API"""
import requests
from sys import argv

if __name__ == "__main__":
    userdata = {"id": argv[1]}
    usertodo = {"userId": argv[1]}
    userurl = "https://jsonplaceholder.typicode.com/users"
    todourl = "https://jsonplaceholder.typicode.com/todos"
    user = requests.get(userurl, params=userdata)
    todo = requests.get(todourl, params=usertodo)
    usuario = user.json()
    remain = todo.json()
    total = len(remain)
    counter = 0
    for itera in remain:
        if itera.get("completed") is True:
            counter += 1
    print("Employee {} is done with tasks({}/{}):".format(usuario[0]["name"],
                                                          counter, total))
    for counter in remain:
        if counter.get("completed") is True:
            print("\t{}".format(counter["title"]))
