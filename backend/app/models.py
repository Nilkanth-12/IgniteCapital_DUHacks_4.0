from django.conf import settings

# Get MongoDB connections
startups_collection = settings.DATABASES['startups_db']['CLIENT']['startups_db']['startups']
investors_collection = settings.DATABASES['investors_db']['CLIENT']['investors_db']['investors']

# Example functions to interact with MongoDB

# Add a startup
def add_startup(name, description, funding_goal):
    startups_collection.insert_one({
        "name": name,
        "description": description,
        "funding_goal": funding_goal
    })

# Add an investor
def add_investor(name, email, investment_amount):
    investors_collection.insert_one({
        "name": name,
        "email": email,
        "investment_amount": investment_amount
    })
