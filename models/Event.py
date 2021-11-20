from mongoengine import Document, StringField


class Event(Document):
    event_id= StringField(max_length=50, required=True)
    investor_id= StringField(max_length=50, required=True)
    name = StringField(max_length=50, required=True)
    host_name = StringField(max_length=50, required=True)
    date= StringField(max_length=50, required=True)
