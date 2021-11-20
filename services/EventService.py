from models.Event import Event
import uuid

def get_event_by_Inv(event_id:str):
    events = Event.objects(event_id=event_id)
    return events
def get_event_count(investor_id:str,sort_by,skip=1,limit=4):
    event_doc = Event.objects(investor_id=investor_id).order_by(sort_by).skip(skip).limit(limit)
    return event_doc

def create_event_by_inv(investor_id:str, event_name: str, event_host_name: str, event_date:str):
    while True:
        gen_event_id = str(uuid.uuid4())[0:7]
        if len(Event.objects(event_id=gen_event_id)) == 0:
            break
    event_doc = Event(event_id=gen_event_id,
                    investor_id=investor_id,
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