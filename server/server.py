from datetime import datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import cors
import db
from models import *

app = FastAPI()
cors.configure_cors(app)

@app.get('/stages')
def fetch_stages():
    stages = jsonable_encoder(db.fetch_stages())
    return JSONResponse(content=stages)

@app.get('/pocs')
def fetch_pocs():
    pocs = jsonable_encoder(db.fetch_pocs())
    return JSONResponse(content=pocs)

@app.get('/pocs/stage/{stage_id}')
def fetch_pocs_for_stage(stage_id: int):
    pocs = jsonable_encoder(db.fetch_pocs_for_stage(stage_id))
    return JSONResponse(content=pocs)

@app.get('/pocs/{poc_id}')
def fetch_one_poc(poc_id: int):
    poc = jsonable_encoder(db.fetch_one_poc(poc_id))
    return JSONResponse(content=poc)

@app.post('/pocs')
def post_new_poc(poc: POC):
    posted_poc = jsonable_encoder(db.post_new_poc(poc))
    return JSONResponse(content=posted_poc)

@app.put('/pocs')
def update_poc(poc: POC):
    updated_poc = jsonable_encoder(db.update_poc(poc))
    return JSONResponse(content=updated_poc)

@app.delete('/pocs/{poc_id}')
def delete_poc(poc_id: int):
    result = jsonable_encoder(db.delete_poc(poc_id))
    return JSONResponse(content=result)

@app.get('/pocs/{poc_id}/uses')
def fetch_uses_for_poc(poc_id: int):
    pocs = jsonable_encoder(db.fetch_uses_for_poc(poc_id))
    return JSONResponse(content=pocs)

@app.post('/pocs/{poc_id}/uses')
def post_new_use(poc_id, use: POCUse):
    posted_use = jsonable_encoder(db.post_new_use(poc_id, use))
    return JSONResponse(content=posted_use)

@app.put('/pocs/{poc_id}/uses')
def update_use(poc_id, use: POCUse):
    updated_use = jsonable_encoder(db.update_use(use))
    return JSONResponse(content=updated_use)


@app.get('/customers')
def get_customers():
    customers = jsonable_encoder(db.fetch_customers())
    return JSONResponse(content=customers)

@app.get('/customers/{customer_id}')
def fetch_one_customer(customer_id: int):
    customer = jsonable_encoder(db.fetch_one_customer(customer_id))
    return JSONResponse(content=customer)

@app.get('/customers/filtered/{search_term}')
def fetch_filtered_customers(search_term: str):
    customers = jsonable_encoder(db.fetch_filtered_customers(search_term))
    return JSONResponse(content=customers)

@app.get('/contacts/{customer_id}')
def fetch_contacts(customer_id: int):
    contacts = jsonable_encoder(db.fetch_contacts(customer_id))
    return JSONResponse(content=contacts)

@app.post('/contacts')
def post_new_contact(contact: Contact):
    posted_contact = jsonable_encoder(db.post_new_contact(contact))
    return JSONResponse(content=posted_contact)

@app.get('/roles')
def fetch_all_roles():
    roles = jsonable_encoder(db.fetch_all_roles())
    return JSONResponse(content=roles)

@app.get('/verticals')
def fetch_all_verticals():
    verticals = jsonable_encoder(db.fetch_all_verticals())
    return JSONResponse(content=verticals)

@app.post('/verticals')
def post_new_vertical(vertical: Vertical):
    posted_vertical = jsonable_encoder(db.post_new_vertical(vertical))
    return JSONResponse(content=posted_vertical)

@app.put('/verticals')
def update_vertical(vertical: Vertical):
    updated_vertical = jsonable_encoder(db.update_vertical(vertical))
    return JSONResponse(content=updated_vertical)
