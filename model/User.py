from mongoengine import Document, StringField


class User(Document):
    name = StringField(max_length=100)
    nick = StringField(max_length=20)
    email = StringField(required=True)
