from models.Fund import Fund
import uuid

def get_fund_by_Inv(fund_id:str):
    funds = Fund.objects(fund_id=fund_id)
    return funds

def get_fund_count(investor_id:str,sort_by,skip=1,limit=4):
    fund_doc = Fund.objects(investor_id=investor_id).order_by(sort_by).skip(skip).limit(limit)
    return fund_doc

def create_fund_by_inv(investor_id:str, fund_amount:str, fund_startup:str, fund_investor:str):  # Service for the POST() method
    while True:
        gen_fund_id = str(uuid.uuid4())[0:7]
        if len(Fund.objects(fund_id=gen_fund_id)) == 0:
            break
    fund_doc = Fund(fund_id=gen_fund_id,
                    investor_id=investor_id,
                    amount=fund_amount,
                    startup_name=fund_startup,
                    investor_name=fund_investor
                    )  # Create a new bank object
    fund_doc.save()  # Save the newly created trip object to the db
    return fund_doc  # Return the list of one trip object that was created

def create_fund_by_inv_SD(investor_id:str, fund_amount:str, fund_startup:str, fund_investor:str):  # Service for the POST() method
    while True:
        gen_fund_id = str(uuid.uuid4())[0:7]
        if len(Fund.objects(fund_id=gen_fund_id)) == 0:
            break
    fund_doc = Fund(fund_id=gen_fund_id,
                    investor_id=investor_id,
                    amount=fund_amount,
                    startup_name=fund_startup,
                    investor_name=fund_investor
                    )  # Create a new bank object
    fund_doc.save()  # Save the newly created trip object to the db
    return fund_doc  # Return the list of one trip object that was created


def delete_fund_by_inv(investor_id: str, fund_id:str):
    fund_doc = Fund.objects(investor_id=investor_id, fund_id=fund_id).first()
    fund_doc.delete()
    sample_response = "Delete successful!"
    return sample_response