from typing import Optional
from pydantic import BaseModel

class Bussines(BaseModel):
    id: Optional[str]
    name: str
    typeOf: str
    photo: str
    lat: float
    lgn: float
    address: str