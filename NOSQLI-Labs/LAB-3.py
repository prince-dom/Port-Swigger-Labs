import requests
import argparse

# def login(Url, username, password):
#     session = requests.Session()
#     print(session)
#     login_url = f"{Url}/login"
#     print(login_url)
#     login_data = {
#         'username': username,
#         'password': password
#     }

#     response = session.post(login_url, data=login_data)
#     print(response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', required=False, dest='username')
    parser.add_argument('-c', required=False, dest='Url')
    parser.add_argument('-p', required=False, dest='password',)
    args = parser.parse_args()
    u = args.Url
    print(u)

    # session = login(args.Url, args.username, args.password)