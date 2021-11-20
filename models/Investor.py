from mongoengine import Document, StringField

class Investor(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email = StringField(max_length=50)
