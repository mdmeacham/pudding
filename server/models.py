from pydantic import BaseModel
from typing import List

class POC(BaseModel):
    id: int
    name: str
    customer_id: int
    stage_id: int
    se_id: int

class POCUse(BaseModel):
    poc_id: int
    use_id: int
    notes: str
    seats: int

class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    title: str
    customer_id: int
    roles: List[int] = []

