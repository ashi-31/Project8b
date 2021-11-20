from mongoengine import Document, StringField

class Transaction(Document):
    number = StringField(max_length=50)
    amount = StringField(max_length=50)
    date_initiated = StringField(max_length=50)
    date_received = StringField(max_length=50)
    investor = StringField(max_length=50)
    startup = StringField(max_length=50)
    status = StringField(max_length=50)
