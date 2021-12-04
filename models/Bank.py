from mongoengine import Document, StringField


class Bank(Document):
    bank_id= StringField(max_length=50, required=True)
    startup_id = StringField(max_length=50, required=True)
    investor_id = StringField(max_length=50, required=True)
    num = StringField(max_length=50, required=True)
    name = StringField(max_length=50, required=True)
    r_num = StringField(max_length=50, required=True)
    check_save= StringField(max_length=50, required=True)
    zip= StringField(max_length=50, required=True)