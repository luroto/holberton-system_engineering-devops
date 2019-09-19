#!/usr/bin/python3
""" This script gets the # of suscribers of a given reddit """
import json
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {"User-Agent": "Requests python library",
               "From": "774@holbertonschool.com"}
    about = requests.get(url, headers=headers)
    about = about.json()
    content = about["data"]
    return (content["subscribers"])
