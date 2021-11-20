from models.Investor import Investor

def get_investor(investor_id: str):  # Service for the GET() method
    if investor_id is None:
        investor_doc = Investor.objects()  # Returning a list of all objects
    else:
        investor_doc = Investor.objects(id=investor_id)  # Returning a list of all objects that match the specific id
    return investor_doc

def get_investor_count(sort_by,skip=1,limit=4):

    investor_doc = Investor.objects().order_by(sort_by).skip(skip).limit(limit)
    return investor_doc

def create_investor(inv_fname: str, inv_lname: str, inv_email: str):  # Service for the POST() method
    investor_doc = Investor(first_name=inv_fname, last_name=inv_lname, email=inv_email)  # Create a new rider object
    investor_doc.save()  # Save the newly created rider object to the db
    return investor_doc  # Return the list of one rider object that was created

def delete_investor(investor_id: str):
    investor_doc = Investor.objects(id=investor_id).first()
    investor_doc.delete()
    sample_response = "Delete successful!"
    return sample_response

def update_investor(investor_id: str, inv_email: str):  # Service for the PATCH() method
    investor_doc = Investor.objects(id=investor_id).first()  # extracting the first object from a list of one object
    investor_doc.update(email=inv_email)
    investor_doc.reload()  # Get the latest copy from the db
    return investor_doc  # Return the list of one rider object that was updated


def init_investors():  # Initialize the db with default riders if there are no existing riders
    existing_investor = Investor.objects()  # List of all rider objects in the db
    if len(existing_investor) == 0:
        inv_fname="Ayushi"
        inv_lname="Jha"
        inv_email="inv0@email.com"
        create_investor(inv_fname, inv_lname, inv_email)