from bson import ObjectId
from backend.model.PeopleModel import People
from backend.connection.MongoDB import connect

class Service(People):
    def __init__(self):
        super().__init__(name="", email="", password="")
        self._client = connect()
        
    def getAllPeoples(self):
        DB = self._client.local
        coll = DB.Peoples
        peoples = list(coll.find()) #recebe a lista de pessoas
        for people in peoples: # 
            people["_id"] = str(people["_id"])
        return peoples
    
    def getPeopleById(self, id):
        DB = self._client.local
        coll = DB.Peoples
        people = coll.find_one({"_id": ObjectId(id)})
        if people:
            people["_id"] = str(people["_id"]) #pega a pessoa e coloca na variavel people
        return people
    
    def addPeople(self, people: People):
        people = People(name=people.name, email=people.email, password=people.password)
        DB = self._client.local
        coll = DB.Peoples
        result = coll.insert_one(people.to_mongo())
    
        return str(result.inserted_id)
    
    def updatePeopleById(self, id, people: People):
        DB = self._client.local
        coll = DB.Peoples
        people = People(name=people.name, email=people.email, password=people.password)
        result = coll.update_one({"_id": ObjectId(id)}, {"$set": people.to_mongo()})
        return result

    def deletePeopleById(self, id):
        DB = self._client.local
        coll = DB.Peoples
        result = coll.delete_one({"_id": ObjectId(id)})
        return result

   