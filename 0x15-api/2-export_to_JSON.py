#!/usr/bin/python3
""" This script gets info from an API and exports it to a JSON file"""
import json
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
    dicto = {}
    listando = []
    for count in remain:
        subdict = {}
        subdict["task"] = count.get("title")
        subdict["completed"] = count.get("completed")
        subdict["username"] = usuario[0].get("username")
        listando.append(subdict)
    dicto[usuario[0].get("id")] = listando
    with open('{}.json'.format(int(argv[1])), 'w') as writingfile:
        json.dump(dicto, writingfile)
