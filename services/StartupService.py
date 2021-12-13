from models.Startup import Startup

def get_startup(startup_id: str):  # Service for the GET() method
    if startup_id is None:
        startup_doc = Startup.objects()  # Returning a list of all objects
    else:
        startup_doc = Startup.objects(id=startup_id)  # Returning a list of all objects that match the specific id
    return startup_doc

def create_startup(startup_ein: str, startup_name: str, startup_email: str):  # Service for the POST() method
    startup_doc = Startup(ein=startup_ein, name=startup_name, email=startup_email)  # Create a new rider object
    startup_doc.save()  # Save the newly created rider object to the db
    return startup_doc  # Return the list of one rider object that was created

def delete_startup(startup_id: str):
    startup_doc = Startup.objects(id=startup_id).first()
    startup_doc.delete()
    return startup_doc

def update_startup(startup_id: str, startup_email: str):  # Service for the PATCH() method
    startup_doc = Startup.objects(id=startup_id).first()  # extracting the first object from a list of one object
    startup_doc.update(email=startup_email)
    startup_doc.reload()  # Get the latest copy from the db
    return startup_doc  # Return the list of one rider object that was updated


def init_startups():  # Initialize the db with default riders if there are no existing riders
    existing_startup = Startup.objects()  # List of all rider objects in the db
    if len(existing_startup) == 0:
        startup_ein="st0"
        startup_name="startup0"
        startup_email="st0@email.com"
        bank={'number':'1111', 'name':'st1', 'r_num':'1110', 'check_save':'C', 'zip_code':'94041'}
        create_startup(startup_ein, startup_name, startup_email,bank)