import threading

from Luna.modules.sql import BASE, SESSION
from sqlalchemy import Column, String


class Pro(BASE):
    __tablename__ = "ot_chats"
    chat_id = Column(String(14), primary_key=True)
    ses_id = Column(String(70))

    def __init__(self, chat_id, ot_grp):
        self.chat_id = chat_id
        self.ot_grp = ot_grp


Pro.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()


def is_chat(chat_id):
    try:
        chat = SESSION.query(Pro).get(str(chat_id))
        if chat:
            return True
        return False
    finally:
        SESSION.close()


def set_ot(chat_id, ot_grp):
    with INSERTION_LOCK:
        autochat = SESSION.query(Pro).get(str(chat_id))
        if not autochat:
            autochat = Pro(str(chat_id), str(ot_grp))
        else:
            autochat.ot_grp = str(ses_id)
            autochat.expires = str(expires)

        SESSION.add(autochat)
        SESSION.commit()


def get_ses(chat_id):
    autochat = SESSION.query(ChatbotChats).get(str(chat_id))
    sesh = ""
    exp = ""
    if autochat:
        sesh = str(autochat.ses_id)
        exp = str(autochat.expires)

    SESSION.close()
    return sesh, exp


def rem_chat(chat_id):
    with INSERTION_LOCK:
        autochat = SESSION.query(ChatbotChats).get(str(chat_id))
        if autochat:
            SESSION.delete(autochat)

        SESSION.commit()


def get_all_chats():
    try:
        return SESSION.query(ChatbotChats.chat_id).all()
    finally:
        SESSION.close()
