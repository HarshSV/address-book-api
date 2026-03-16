from pydantic import BaseModel

class AddressCreate(BaseModel):
    name: str
    street: str
    city: str
    latitude: float
    longitude: float