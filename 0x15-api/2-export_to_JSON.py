#!/usr/bin/python3
""" This script gets info from an API and exports to a JSON file"""
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
    subdict = {}
    subdict["username"] = usuario[0].get("username")
    dicto = {}
    listando = []
    for count in remain:
        for key, value in count.items():
            if key == "title" or key == "completed":
                subdict[key] = value
                listando.append(subdict)
    print(len(subdict.keys()))
    dicto[usuario[0].get("id")] = listando
    listando.append(subdict)
    with open('{}.json'.format(int(argv[1])), 'w') as writingfile:
        json.dump(dicto, writingfile)
