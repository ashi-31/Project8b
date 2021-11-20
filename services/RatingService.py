from models.Rating import Rating
import uuid

def get_rating_by_Inv(investor_id: str):
    ratings = None
    if investor_id is not None:
        ratings = Rating.objects(investor_id=investor_id)
    return ratings

def create_rating_by_inv(investor_id:str, rating_value: str, rating_profile: str):
    while True:
        gen_rating_id = str(uuid.uuid4())[0:7]
        if len(Rating.objects(rating_id=gen_rating_id)) == 0:
            break
    rating_doc = Rating(rating_id=gen_rating_id,
                    investor_id=investor_id,
                    value=rating_value,
                    profile=rating_profile,
                    )
    rating_doc.save()
    return rating_doc

def delete_rating_by_inv(investor_id: str, rating_id:str):
    rating_doc = Rating.objects(investor_id=investor_id, rating_id=rating_id).first()
    rating_doc.delete()
    sample_response = "Delete successful!"
    return sample_response