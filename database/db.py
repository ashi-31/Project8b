from flask_mongoengine import MongoEngine
from services.InvestorService import init_investors
from services.StartupService import init_startups
from services.TransactionService import init_transactions

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)  # Create the db
    init_investors()
    init_startups()
    init_transactions()


def fetch_engine():
    return db
