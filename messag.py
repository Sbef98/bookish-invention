from instadm import InstaDM

def get_login_credentials():
    f = open("credentials.credentials", "rt")
    lines = f.readlines()
    f.close()
    lines[0] = lines[0].split("\n")[0]
    lines[1] = lines[1].split("\n")[0]
    return lines

# Auto login
insta = InstaDM(username=get_login_credentials()[0], password=get_login_credentials()[1], headless=True)

# Send message
insta.sendMessage(user='mattia_faraci', message='Hey !')

# Send message
#insta.sendGroupMessage(users=['user1', 'user2'], message='Hey !')