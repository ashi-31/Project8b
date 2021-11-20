from mongoengine import Document, StringField


class Startup(Document):
    ein = StringField(max_length=50)
    name = StringField(max_length=50)
    email = StringField(max_length=50)