from mongoengine import Document, StringField


class Fund(Document):
    fund_id= StringField(max_length=50, required=True)
    investor_id= StringField(max_length=50, required=True)
    amount = StringField(max_length=50, required=True)
    startup_name = StringField(max_length=50, required=True)
    investor_name= StringField(max_length=50, required=True)

