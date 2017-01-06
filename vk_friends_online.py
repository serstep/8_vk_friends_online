import vk
from getpass import getpass


APP_ID = "5808265" 


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
        print("Yor friends online:\nid: {uid}\nfirst name: {first_name}\nlast name: {last_name}\n".\
            format(**friend))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()

    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError :
        print("The username and/or password you specified are not correct.")
        exit(1)

    output_friends_to_console(friends_online)
