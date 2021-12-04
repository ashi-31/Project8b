from models.Event import Event
import uuid

def get_event(event_id: str):  # Service for the GET() method
    if event_id is None:
        event_doc = Event.objects()  # Returning a list of all objects
    else:
        event_doc = Event.objects(id=event_id)  # Returning a list of all objects that match the specific id
    return event_doc
def get_event_by_Inv(investor_id:str,event_id:str):
    events = None
    if investor_id is not None and event_id is not None:
        events = Event.objects(event_id=event_id)  # Returning all objects that matches the specific id
    elif investor_id is not None and event_id is None:
        events = Event.objects(investor_id=investor_id)
    return events
def get_event_by_str(startup_id:str,event_id:str):
    events = None
    if startup_id is not None and event_id is not None:
        events = Event.objects(event_id=event_id)  # Returning all objects that matches the specific id
    elif startup_id is not None and event_id is None:
        events = Event.objects(startup_id=startup_id)
    return events
def get_event_count_inv(investor_id:str,sort_by,skip=1,limit=4):
    event_doc = Event.objects(investor_id=investor_id).order_by(sort_by).skip(skip).limit(limit)
    return event_doc
def get_event_count_str(startup_id:str,sort_by,skip=1,limit=4):
    event_doc = Event.objects(startup_id=startup_id).order_by(sort_by).skip(skip).limit(limit)
    return event_doc
def create_event(eve_name:str,eve_host_name:str,eve_date:str):  # Service for the POST() method
    event_doc = Event(name=eve_name, host_name=eve_host_name, date=eve_date)  # Create a new rider object
    event_doc.save()  # Save the newly created rider object to the db
    return event_doc  # Return the list of one rider object that was created
def create_event_by_inv(investor_id:str, event_name: str, event_host_name: str, event_date:str):
    while True:
        gen_event_id = str(uuid.uuid4())[0:7]
        if len(Event.objects(event_id=gen_event_id)) == 0:
            break
    event_doc = Event(event_id=gen_event_id,
                    investor_id=investor_id,
                    startup_id="None",
                    name=event_name,
                    host_name=event_host_name,
                    date=event_date
                    )
    event_doc.save()  # Save the newly created trip object to the db
    return event_doc

def create_event_by_str(startup_id:str, event_name: str, event_host_name: str, event_date:str):
    while True:
        gen_event_id = str(uuid.uuid4())[0:7]
        if len(Event.objects(event_id=gen_event_id)) == 0:
            break
    event_doc = Event(event_id=gen_event_id,
                    investor_id="None",
                    startup_id=startup_id,
                    name=event_name,
                    host_name=event_host_name,
                    date=event_date
                    )
    event_doc.save()  # Save the newly created trip object to the db
    return event_doc

def delete_event_by_inv(investor_id: str, event_id:str):
    event_doc = Event.objects(investor_id=investor_id, event_id=event_id).first()
    event_doc.delete()
    sample_response = "Delete successful!"
    return sample_response