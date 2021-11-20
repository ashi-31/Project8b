from models.Transaction import Transaction

def get_transaction(transaction_id: str):  # Service for the GET() method
    if transaction_id is None:
        transaction_doc = Transaction.objects()  # Returning a list of all objects
    else:
        transaction_doc = Transaction.objects(id=transaction_id)  # Returning a list of all objects that match the specific id
    return transaction_doc

def get_transaction_count(sort_by,skip=1,limit=1000):
    transaction_doc = Transaction.objects().order_by(sort_by).skip(skip).limit(limit)
    return transaction_doc

def create_transaction(tr_number: str, tr_amount: str, tr_date_initiated: str, tr_date_received: str, tr_investor:str, tr_startup:str, tr_status:str):  # Service for the POST() method
    transaction_doc = Transaction(number=tr_number, amount=tr_amount, date_initiated=tr_date_initiated, date_received=tr_date_received, investor=tr_investor, startup= tr_startup, status= tr_status )  # Create a new rider object
    transaction_doc.save()  # Save the newly created rider object to the db
    return transaction_doc  # Return the list of one rider object that was created

def delete_transaction(transaction_id: str):
    transaction_doc = Transaction.objects(id=transaction_id).first()
    transaction_doc.delete()
    sample_response = "Delete successful!"
    return sample_response

def update_transaction(transaction_id: str, tr_status: str):  # Service for the PATCH() method
    transaction_doc = Transaction.objects(id=transaction_id).first()  # extracting the first object from a list of one object
    transaction_doc.update(status=tr_status)
    transaction_doc.reload()  # Get the latest copy from the db
    return transaction_doc  # Return the list of one rider object that was updated


def init_transactions():  # Initialize the db with default riders if there are no existing riders
    existing_transaction = Transaction.objects()  # List of all rider objects in the db
    if len(existing_transaction) == 0:
        tr_number="010101"
        tr_amount="50000"
        tr_date_initiated="11152021"
        tr_date_received="11182021"
        tr_investor= "inv01"
        tr_startup= "st01"
        tr_status= "pending"
        create_transaction(tr_number, tr_amount, tr_date_initiated, tr_date_received, tr_investor, tr_startup, tr_status)