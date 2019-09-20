#!/usr/bin/python3
""" This script gets the # of suscribers of a given reddit """
import json
import requests


def number_of_subscribers(subreddit):
    """ This is the module to be imported which get the answer"""
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {"User-Agent": "Requests python library",
               "From": "774@holbertonschool.com"}
    about = requests.get(url, headers=headers, allow_redirects=False)
    if about.status_code > 300:
        return(0)
    about = about.json()
    content = about["data"]
    return (content["subscribers"])
