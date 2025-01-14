from fastapi import FastAPI
from typing import Union
from backend.model.PeopleModel import People
from backend.service.PeopleService import Service

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/people/add")
def addPeople(people: Union[People, dict]):
    if isinstance(people, People):
        service = Service()
        service = service.addPeople(people)
        return people
    elif isinstance(people, dict):
        return People(**people)
    else:
        return None

@app.get("/people/all") 
def getAllPeoples():
    service = Service()
    peoples = service.getAllPeoples()
    return peoples

@app.get("/people/id/{id}")
def getPeopleById(id: str):
    service = Service()
    people = service.getPeopleById(id)
    return people

@app.get("/people/name/{name}")
def getPeopleByName(name: str):
    name = name.replace("%20", " ")
    service = Service()
    people = service.getPeopleByName(name)
    return people

@app.put("/people/update/{id}")
def updatePeopleById(id: str, people: People):
    service = Service()
    service.updatePeopleById(id, people)
    return people

@app.delete("/people/delete/{id}")
def deletePeopleById(id: str):
    service = Service()
    service.deletePeopleById(id)
    return {"message": "People deleted successfully"}