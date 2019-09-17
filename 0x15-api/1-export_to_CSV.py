#!/usr/bin/python3
""" This script gets info from an API"""
import csv
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
    lista = []
    for itera in remain:
        if itera.get("completed") is True:
            counter += 1
        appending = [usuario[0].get("id"), usuario[0].get("username"),
                     itera.get("completed"), itera.get("title")]
        lista.append(appending)
    with open('{}.csv'.format(int(argv[1])), 'w', newline='') as writingfile:
        writing = csv.writer(writingfile, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL)
        for iteran in lista:
            writing.writerow(iteran)
