# -*- coding: utf-8 -*-
"""
Test Module for User and Mail
"""

import unittest
from main import User, Mail, send_mail_to_users


class MailSenderTest(unittest.TestCase):
    """Test mail sender (send_mail_to_users)"""

    def setUp(self):
        self.new_mail = Mail('<EMAIL_TOPIC>', '<EMAIL_BODY>')
        self.user_1 = User('<USER_NAME_1>', '<USER_EMAIL_1>')
        self.user_2 = User('<USER_NAME_2>', '<USER_EMAIL_2>')
        self.user_3 = User('<USER_NAME_3>', '<USER_EMAIL_3>')

    def test_sender_not_in_recipients(self) -> None:
        """Test that sender is not in recipients"""
        self.assertEqual(
            send_mail_to_users(self.new_mail, self.user_1, [self.user_1, self.user_2]),
            "Отправителя не должно быть в получателях",
            "Error: sender in recipients")

    def test_send_mail_to_users_successfully(self) -> None:
        send_mail_to_users(self.new_mail, self.user_1, [self.user_3, self.user_2])
        self.assertEqual(self.new_mail.sender, self.user_1, "Error: sender not set")
