from instadm import InstaDM

db = r".\Database\instadms.db"
sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users_to_write (
                                    username text PRIMARY KEY,
                                ); """
sql_create_already_contacted_table = """ CREATE TABLE IF NOT EXISTS already_contacted (
                                    username text PRIMARY KEY,
                                ); """

def get_login_credentials():
    f = open("credentials.credentials", "rt")
    lines = f.readlines()
    f.close()
    lines[0] = lines[0].split("\n")[0]
    lines[1] = lines[1].split("\n")[0]
    return lines

def update_database(file_name = "./settings/users.list"):
    #get_all_users_list
    f = open(file_name, "rt")
    lines = f.readline()
    f.close()

    users = lines.pop(0)



if __name__ == "__main__":
    # Auto login
    insta = InstaDM(username=get_login_credentials()[0], password=get_login_credentials()[1], headless=True)

    # Send message
    insta.sendMessage(user='mattia_faraci', message='Hey !')

    # Send message
    #insta.sendGroupMessage(users=['user1', 'user2'], message='Hey !')