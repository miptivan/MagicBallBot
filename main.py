import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


token = "03d29bb33f31c2868fba7346b095a6ab79bdd2fcb161f2c06644738dc4235d532dc4a3527be9ef9f604fa"
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


def userinfo(id):
    return vk_session.method('users.get', {'user_ids': id})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.message.lower()
            id = event.user_id
            if msg == 'привет':
                a = userinfo(id)
                print(a)
                sender(id, 'вечер в хату, ' + a[0]['first_name'])
