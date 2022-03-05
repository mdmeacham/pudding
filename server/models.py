from pydantic import BaseModel

class POC(BaseModel):
    id: int
    name: str
    customer_id: int
    stage_id: int
    se_id: int

class Use(BaseModel):
    id: int
    name: str
    description: str
    seats: int
    poc_id: int

def test_model(poc: POC):
    print(poc)