# ======================================================================================================================
# Source: https://www.w3schools.com/python/python_mongodb_getstarted.asp  (COMPLETED AND REVISED 2/2023)
# Watch tech with tim:
# 1. https://www.youtube.com/watch?v=UpsZDGutpZc
# 2. https://www.youtube.com/watch?v=nYNAH8K_UhI
# 3.


# --  USE https://dbfiddle.uk/  to practice queries
# https://www.mongodb.com/kafka-connector
# ======================================================================================================================
# MongoDB   Data is stored in the form of JSON style documents. Faster, dynamic queries (flexible, scalable)
#           horizontally scalable i.e we can add more servers (sharding compliant)
#           emphasizes on the CAP theorem (Consistency, Availability, and Partition tolerance)
#           RDBMS is only vertically scalable i.e increasing RAM and emphasis is on ACID properties
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------
# RDBMS    MongoDB
# ----------------------------------------------------------------------------------------------------------------------
#        = CLUSTER  (set of databases are on a cluster)
# TABLE  = COLLECTION
# RECORD = DOCUMENT (upper limit = 16MB / document)

# ======================================================================================================================
# Products:
# ======================================================================================================================
# 1. MongoDB CLI
# 2. MongoDB Compass GUI: An interactive GUI to explore, query, and manage your data on MongoDB
# 3. MongoDB Shell: A modern shell experience for interacting with your data in MongoDB.
# 4. Ops Manager
# 5. MongoDB extension for VS CODE

# ======================================================================================================================
# Install MongoDB on Windows 10. Requires Windows 10+ / Server 2016+
# https://www.mongodb.com/try/download/community  -> Select Package -> MSI
# Current Version 10/21/2021 = 7.0.4 (mongodb-windows-x86_64-7.0.4-signed.msi)
# has option to install MongoDB Compass
# Python uses the MongoDB driver "PyMongo" Requires: python -m pip install pymongo

# ======================================================================================================================
# MongoDB waits until you have created a collection (table), with at least one document (record)
#         before it actually creates the database (and collection)
# MongoDB uses Change Streams API for triggering
# MongoDB works with JSON or BSON = Binary JSON https://www.mongodb.com/json-and-bson
# MongoDB more flexible format than RDBMS.  Can add documents with any schema to a collection
# ======================================================================================================================

from datetime import date
from dateutil.parser import parse
from pprint import pprint
from bson.objectid import ObjectId  # binary json - requires `pip install bson` appears to be a dependency for pymongo
import pymongo

# Connect to your MongoDB cluster:
client = pymongo.MongoClient("mongodb://localhost:27017/")  # thread-safe and has connection-pooling built in
# If an operation fails because of a network error, ConnectionFailure
# is raised and the client reconnects in the background.

client  # returns MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
db = client["testdb"]  # add a database, or access if already exists
db = client.testdb     # same as above

customer_collection = db["customers"]  # This is a collection / Table
customer_collection = db.customers     # same as above, will create if doesn't exist, only assign if exists
# customer_collection = db.create_collection('customers')  this will fail if exists with "pymongo.errors.CollectionInvalid"

customer_collection  # Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'testdb'), 'customers')

client.list_database_names()    # Return a list of your system's databases   ['admin', 'local', 'testdb']
db.list_collection_names()      # Returns list of collections/tables         ['customers']

# INSERT ONE RECORD (Called Document) you do not specify an "_id" field, then MongoDB will add one for you
x = customer_collection.insert_one({"name": "Peter", "address": "Lowstreet 27"})
x  # InsertOneResult(ObjectId('659224d0a4944e477a84c993'), acknowledged=True)
x.inserted_id  # Returns a bson ObjectId e.g. 659224d0a4944e477a84c993
customer_collection.find_one()  # Returns {'_id': ObjectId('659224d0a4944e477a84c993'), 'name': 'Peter', 'address': 'Lowstreet 27'}
customer_collection.find_one({"_id": ObjectId(x.inserted_id)})   # same as above  since only one record in the collection

# INSERT MANY RECORDS (Called Documents), _id is the primary key in mongodb, can store date/datetime objects
mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37", "joined": "2023, 1, 1"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27", "joined": "2023, 1, 1"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652", "joined": "2023, 1, 1"}]
x = customer_collection.insert_many(mylist)
x.inserted_ids     # Returns [ObjectId('5b19112f2ddb101964065487'), ObjectId('5b19112f2ddb101964065488'), ObjectId('5b19112f2ddb101964065489')]


# SELECT COMMANDS
customer_collection.find_one()            # Returns 1st record in the table or of your query
customer_collection.find_one({"joined": "2023, 1, 1"})  # returns first record that matches the filter
x = customer_collection.find()            # Returns iterator, record type = pymongo.cusor.Cursor of all records
x = customer_collection.find().limit(5)   # Returns top five
x = customer_collection.find({"address": "Highway 37"})  # Return WHERE address="Highway 37"
x = customer_collection.find({}, {"_id": 0, "name": 1, "address": 1})    # Return Name, Address columns only, exclude _id column
x = customer_collection.find({}, {"address": 0}) # Return all columns accept the address column

# The Greater Than Modifier.  gt=greater_than, lt=less_than, gte=greater_than_or_equal, lte=less_than_or_equal
query1 = {"address": {"$gte": "S"}}
x = customer_collection.find(query1)   # Return WHERE "address" field starts with the letter "S" or higher (alphabetically)
query2 = {"age": {"$lt": "53"}}
x = customer_collection.find({"$and": [query1, query2]})  # combined query
x = customer_collection.find({"$or": [query1, query2]})  # combined query

# The Regex Modifier
x = customer_collection.find({"address": {"$regex": "^S"}})  # address starts with the letter "S"

# ORDER BY
x = customer_collection.find().sort("name", -1)  # ORDER BY NAME DESCENDING

# COUNT
customer_collection.count_documents(filter={})   # counts documents that match the filter

# DELETE
customer_collection.delete_one({"address": "Mountain 21"})  # deletes the first record that matches query
x = customer_collection.delete_many({"address": {"$regex": "^S"}}) # deletes all records that match regex
x = customer_collection.delete_many({})  # delete all records
x.deleted_count  # from last query

# UPDATE ONE
customer_collection.insert_one({"name": "Frankie", "address": "Valley 345", "age": 54, "gender": "m"})
myquery = {"address": "Valley 345"}
newvalues = { "$set": { "address": "Canyon 123" } }   # not sure what "$unset" does
customer_collection.update_one(myquery, newvalues)


# UPDATE MANY
customer_collection.insert_one({"name": "Frankie", "address": "Road 534", "age": 32, "gender": "m"})
query = {"name": "Frankie"}
updates = {"$set": {"name": "Frank"},
           "$rename": {"gender": "sex", "address": "location"},
           "$inc": {"age": 1}}
x = customer_collection.update_many(query, updates)   # UpdateResult({'n': 2, 'nModified': 2, 'ok': 1.0, 'updatedExisting': True}, acknowledged=True)
# updates all Frankies to Frank, renames the 'name' field, and increments their ages

# REPLACE ONE
# customer_collection.replace_one({"_id": ObjectId(object_ID)}, new_document)   # this swaps out the full document for a new one

# DROP COLLECTION
customer_collection.drop() #  returns true if the collection was dropped successfully, and false if the collection does not exist.


# mongodb_document = {
#     “_id”: ObjectId(“617c1f77a6f4441a0c0f1a0a”),
#     “tradeId”: “Trade1234”,
#     “security”: “MDB”,
#     “action”: “BUY”,
#     “shares”: 200,
#     “creationDate”: ISODate(“2023 - 10 - 09T09: 00: 00Z”),
#     “executions”: [{
#             “executionId”: “EXEC5678”,
#             “Shares”: 200,
#             “executionPrice”: 150.00,
#             “executionDate”: ISODate(“2023 - 10 - 09T10: 00: 00Z”)
#         }
#     ]
#     foreign_key = "5b19112f2ddb101964065487"   <-- association to an _id in a different collection
# }

# import pyarrow
# import pymongoarrow

dbname =  client['sample_mflix']

# Create a new collection
collection_name = dbname["user_1_items"]

# Create an index on the collection
category_index = collection_name.create_index("category")
category_index  # 'category_1'

collection_name = dbname["user_1_items"]
collection_name.drop()  # purges all previous rows - otherwise you'll get a duplicate error - will not fail silently as you have used  "_id" for item_1 & item_2

item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}

item_2 = {
  "_id" : "U1IT00002",
  "item_name" : "Egg",
  "category" : "food",
  "quantity" : 12,
  "price" : 36,
  "item_description" : "brown country eggs"
}

collection_name.insert_many([item_1, item_2])

expiry_date = "2024-01-01T00:00:00.000Z"

expiry = parse( expiry_date )  # returns datetime object datetime.datetime(2024, 1, 1, 0, 0, tzinfo=tzutc())

item_3 = {
  "item_name" : "Bread",
  "quantity" : 2,
  "ingredients" : "all-purpose flour",
  "expiry_date" : expiry
}
collection_name.insert_one(item_3)

# collection_name.insert_one({'date': date(2021, 1, 1)})  <-- this will fail
# bson.errors.InvalidDocument: cannot encode object: datetime.date(2021, 1, 1), of type: <class 'datetime.date'>

# Retrieve a collection named "user_1_items" from database
collection_name = dbname["user_1_items"]
item_details = collection_name.find()
collection_name.drop()

db = client["sample_mflix"]  # Get a reference to the "sample_mflix" database
movie_collection = db["movies"]  # Get a reference to the "movies" collection
stage_match_title = {"$match": {"title": "A Star Is Born"}}   # Match title = "A Star Is Born":
stage_sort_year_ascending = {"$sort": { "year": pymongo.DESCENDING}}  # Sort by year, ascending
stage_limit_1 = {"$limit": 1}  # Limit to 1 document:

# Now the pipeline is easier to read:
pipeline = [
   stage_match_title,
   stage_sort_year_ascending,
    stage_limit_1
]

results = movie_collection.aggregate(pipeline)
for movie in results:
   print(" * {title}, {first_castmember}, {year}".format(
         title=movie["title"],
         first_castmember=movie["cast"][0],
         year=movie["year"],
   ))

# Look up related documents in the 'comments' collection:
stage_lookup_comments = {
   "$lookup": {
         "from": "comments",
         "localField": "_id",
         "foreignField": "movie_id",
         "as": "related_comments",
   }
}

# Limit to the first 5 documents:
stage_limit_5 = { "$limit": 5 }

pipeline = [
   stage_lookup_comments,
   stage_limit_5,
]

results = movie_collection.aggregate(pipeline)
for movie in results:
   pprint(movie)


# collection.aggregate(pipeline)   # c.f with GROUP BY ... HAVING command
# collection.watch()
# collection.bulk_write()
# MongoDb Transactions