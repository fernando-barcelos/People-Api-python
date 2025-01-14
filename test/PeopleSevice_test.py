from backend.model.PeopleModel import People
from backend.service.PeopleService import Service
import pytest

@pytest.mark.asyncio
class  test_PeopleService:
    async def test_add_People(self):
        # Setup
        people = People(name="John Doe", email="johndoe@example.com", password="password123")

        # Test adding People
        result = Service.addPeople(self, people)
        assert result is not None
        assert result.id is not None
        assert result.name == "John Doe"
        assert result.email == "johndoe@example.com"
        assert result.password == "password123"
