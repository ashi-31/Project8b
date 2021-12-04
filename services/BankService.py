from models.Bank import Bank
import uuid

def get_bank_by_Inv(investor_id:str, bank_id:str):  # Service for the GET() method
    banks=None
    if investor_id is not None and bank_id is not None:
        banks = Bank.objects(bank_id=bank_id)  # Returning all objects that matches the specific id
    elif investor_id is not None and bank_id is None:
        banks = Bank.objects(investor_id=investor_id)
    return banks

def get_bank_by_str(startup_id, bank_id=None):  # Service for the GET() method
    banks=None
    if startup_id is not None and bank_id is not None:
        banks = Bank.objects(bank_id=bank_id)  # Returning all objects that matches the specific id
    elif startup_id is not None and bank_id is None:
        banks = Bank.objects(startup_id=startup_id)
    return banks

def create_bank_by_inv(investor_id:str,bank_num: str, bank_name: str, bank_r_num: str, bank_check_save: str, bank_zip:str):  # Service for the POST() method
    while True:
        gen_bank_id = str(uuid.uuid4())[0:7]
        if len(Bank.objects(bank_id=gen_bank_id)) == 0:
            break
    bank_doc = Bank(investor_id=investor_id,
                    startup_id="None",
                    bank_id=gen_bank_id,
                    num=bank_num,
                    name=bank_name,
                    r_num=bank_r_num,
                    check_save=bank_check_save,
                    zip=bank_zip
                    )  # Create a new bank object
    bank_doc.save()  # Save the newly created trip object to the db
    return bank_doc  # Return the list of one trip object that was created

def create_bank_by_str(startup_id:str,bank_num: str, bank_name: str, bank_r_num: str, bank_check_save: str, bank_zip:str):  # Service for the POST() method
    while True:
        gen_bank_id = str(uuid.uuid4())[0:7]
        if len(Bank.objects(bank_id=gen_bank_id)) == 0:
            break
    bank_doc = Bank(startup_id=startup_id,
                    investor_id="None",
                    bank_id=gen_bank_id,
                    num=bank_num,
                    name=bank_name,
                    r_num=bank_r_num,
                    check_save=bank_check_save,
                    zip=bank_zip
                    )  # Create a new bank object
    bank_doc.save()
    return bank_doc

def patch_bank_by_Inv(investor_id: str,bank_id:str, bank_name:str):  # Service for the GET() method
    bank_doc = Bank.objects(investor_id=investor_id, bank_id=bank_id).first()  # extracting the first object from a list of one object
    bank_doc.update(name=bank_name)
    bank_doc.reload()  # Get the latest copy from the db
    return bank_doc  # Return the list of one rider object that was updated

def patch_bank_by_str(startup_id:str,bank_id:str, bank_name:str):  # Service for the GET() method
    bank_doc = Bank.objects(startup_id=startup_id, bank_id=bank_id).first()  # extracting the first object from a list of one object
    bank_doc.update(name=bank_name)
    bank_doc.reload()  # Get the latest copy from the db
    return bank_doc  # Return the list of one rider object that was updated

def delete_bank_by_inv(investor_id: str, bank_id:str):
    bank_doc = Bank.objects(investor_id=investor_id, bank_id=bank_id).first()
    bank_doc.delete()
    sample_response = "Delete successful!"
    return sample_response

