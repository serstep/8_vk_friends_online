import vk
from getpass import getpass


APP_ID = "5808265"  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return input("Type your login ")


def get_user_password():
    return getpass("Type your password ")
    

def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    
    friends_online_ids = api.friends.getOnline()
    friends_online_list = api.users.get(user_ids=friends_online_ids)
    return friends_online_list


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print("Yor friends online:\nid: {}\nfirst name: {}\nlast name: {}\n".\
            format(friend["uid"], friend["first_name"], friend["last_name"]))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
