# Python version >= 3.10
"""Main module"""


class User:
    """User class"""

    def __init__(self, user_name: str, user_email: str):
        self.name: str = user_name
        self.email: str = user_email
        self.sent_mails: list[Mail] = []
        self.received_mails: list[Mail] = []


class Mail:
    """Mail class"""

    def __init__(self, mail_topic: str, mail_text: str):
        self.topic: str = mail_topic
        self.text: str = mail_text
        self._sender: User | None = None
        self.recipients: list[User] = []

    @property
    def sender(self):
        """ Sender of the mail
        :return:
        """
        return self._sender

    @sender.setter
    def sender(self, sender: User):
        self._sender = sender

    @sender.getter
    def sender(self):
        return self._sender


def send_mail_to_users(mail_to_send: Mail,
                       sender_user: User,
                       recipients: list[User]) -> str:
    """
    :param mail_to_send:
    :param sender_user:
    :param recipients:
    :return str:
    """
    mail_to_send.sender = sender_user
    sender_user.sent_mails.append(mail_to_send)
    if mail_to_send.sender in recipients:
        return "Отправителя не должно быть в получателях"
    for recipient in recipients:
        recipient.received_mails.append(mail_to_send)
    return "Ок"
