from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Address Book API")


@app.post("/address/")
def create_address(address: schemas.AddressCreate, db: Session = Depends(database.get_db)):
    return crud.create_address(db, address)


@app.get("/address/")
def get_addresses(db: Session = Depends(database.get_db)):
    return crud.get_addresses(db)


@app.put("/address/{address_id}")
def update_address(address_id: int, address: schemas.AddressCreate, db: Session = Depends(database.get_db)):
    return crud.update_address(db, address_id, address)


@app.delete("/address/{address_id}")
def delete_address(address_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_address(db, address_id)