from mongoengine import Document, StringField


class Rating(Document):
    rating_id= StringField(max_length=50, required=True)
    investor_id= StringField(max_length=50, required=True)
    value = StringField(max_length=50, required=True)
    profile = StringField(max_length=50, required=True)
