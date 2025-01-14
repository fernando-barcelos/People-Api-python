
from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class People(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    password: str

    class Config:
        name = "people"
        json_encoders = {
            ObjectId: str
        }

    def to_mongo(self):
        if not self.id:
            self.id = str(ObjectId())
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
