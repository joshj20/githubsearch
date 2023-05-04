import json, requests
import qf

def getusr():
    qf.cls()
    username = input('Type the github username to be searched: ')
    url = "https://api.github.com/users/%s" % (username)
    response = requests.get(url=url)
    class user(object):
        def __init__(self, data):
            self.__dict__ = json.loads(data)
    userdata = user(response.text)
    print('\n')
    try:
        print('Name:', userdata.name)
        print('GitHub url:', userdata.html_url)
        print('Type of account:', userdata.type)
        print('Lives in:', userdata.location)
        print('Email Address:', userdata.email)
        print('Bio:', userdata.bio)
        print('Followers: ', userdata.followers)
        print(userdata.name, 'Is Following', userdata.following, 'People')
        qf.br()
        re_search = input("Do you want another github user's information? (Y/N): ")
        if re_search.lower() == 'y':
            getusr()
        else:
            return 0
    except:
        print('Username Not Found. Please Try Again.')
        re_search = input("Do you want to try again? (Y/N): ")
        if re_search.lower() == 'y':
            getusr()
        else:
            return 1

getusr()