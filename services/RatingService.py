from models.Rating import Rating
import uuid

def get_rating(rating_id: str):  # Service for the GET() method
    if rating_id is None:
        rating_doc = Rating.objects()  # Returning a list of all objects
    else:
        rating_doc = Rating.objects(id=rating_id)  # Returning a list of all objects that match the specific id
    return rating_doc
def get_rating_by_Inv(investor_id:str, rating_id:str):  # Service for the GET() method
    ratings=None
    if investor_id is not None and rating_id is not None:
        ratings = Rating.objects(rating_id=rating_id)  # Returning all objects that matches the specific id
    elif investor_id is not None and rating_id is None:
        ratings = Rating.objects(investor_id=investor_id)
    return ratings

def get_rating_by_str(startup_id, rating_id=None):  # Service for the GET() method
    ratings=None
    if startup_id is not None and rating_id is not None:
        ratings = Rating.objects(rating_id=rating_id)  # Returning all objects that matches the specific id
    elif startup_id is not None and rating_id is None:
        ratings = Rating.objects(startup_id=startup_id)
    return ratings

def create_rating_by_inv(investor_id:str,rating_value:str, rating_profile:str):  # Service for the POST() method
    while True:
        gen_rating_id = str(uuid.uuid4())[0:7]
        if len(Rating.objects(rating_id=gen_rating_id)) == 0:
            break
    rating_doc = Rating(investor_id=investor_id,
                    startup_id="None",
                    rating_id=gen_rating_id,
                    value=rating_value,
                    profile=rating_profile
                    )  # Create a new bank object
    rating_doc.save()  # Save the newly created trip object to the db
    return rating_doc  # Return the list of one trip object that was created

def create_rating_by_str(startup_id:str,rating_value:str, rating_profile:str):  # Service for the POST() method
    while True:
        gen_rating_id = str(uuid.uuid4())[0:7]
        if len(Rating.objects(rating_id=gen_rating_id)) == 0:
            break
    rating_doc = Rating(startup_id=startup_id,
                    investor_id="None",
                    rating_id=gen_rating_id,
                    value=rating_value,
                    profile=rating_profile
                    )  # Create a new bank object
    rating_doc.save()  # Save the newly created trip object to the db
    return rating_doc  # Return the list of one trip object that was created

def delete_rating_by_inv(investor_id: str, rating_id:str):
    rating_doc = Rating.objects(investor_id=investor_id, rating_id=rating_id).first()
    rating_doc.delete()
    sample_response = "Delete successful!"
    return sample_response