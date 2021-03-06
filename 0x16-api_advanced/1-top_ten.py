#!/usr/bin/python3
""" This script prints the top ten hot post of a given subreddit"""
import requests


def top_ten(subreddit):
    """ This script gets and processes the http response"""
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    identify = {"User-Agent": "Requests library from Python",
                "From": "774@holbertonschool.com"}
    to_print = []
    hot = requests.get(url, headers=identify, allow_redirects=False)
    if hot.status_code == 404:
        print("None")
        return 0
    if hot.status_code == 200:
        hot = hot.json()
        hot = hot["data"]
        hot = hot["children"]
        for items in hot:
            del items["kind"]
        for data in hot:
            to_print.append(data["data"])
        hot = to_print
        to_print = []
        for dictio in hot:
            to_print.append(dictio["title"])
        for itera in to_print:
            print(itera)
