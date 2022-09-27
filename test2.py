import pymongo


client = pymongo.MongoClient("mongodb+srv://SNEHA:SNEHA@SNEHA."
                             "d0xirlw.mongodb.net/?retryWrites=true&w=majority")

db1 = client["test1"]
coll = db1['test']

record = coll.find()

# for i in record:-
#    print(i)

# data = coll.find({"CompanyName": "INeuron"})

data = coll.find({"Course Offered": {"$gt": "E"}})
for i in data:
    print(i)

