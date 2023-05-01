from typing import List

from fastapi import FastAPI, Depends, HTTPException, status, Path, Query
from sqlalchemy.orm import Session
from sqlalchemy import text

from db import get_db
from models import Owner, Cat
from schemas import OwnerModel, OwnerResponse, CatModel, CatResponse, CatVaccinatedModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        # Make request
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")


@app.get("/owners", response_model=List[OwnerResponse], tags=["owners"])
async def get_owners(db: Session = Depends(get_db)):
    owners = db.query(Owner).all()
    return owners


@app.get("/owners/{owner_id}", response_model=OwnerResponse, tags=["owners"])
async def get_owner(owner_id: int = Path(ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return owner


@app.post("/owners", response_model=OwnerResponse, tags=["owners"])
async def create_owner(body: OwnerModel, db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(email=body.email).first()
    if owner:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is exists!")
    owner = Owner(email=body.email)  # Owner(**body.dict())
    db.add(owner)
    db.commit()
    return owner


@app.put("/owners/{owner_id}", response_model=OwnerResponse, tags=["owners"])
async def update_owner(body: OwnerModel, owner_id: int = Path(ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    owner.email = body.email
    db.commit()
    return owner


@app.delete("/owners/{owner_id}", response_model=OwnerResponse, tags=["owners"])
async def delete_owner(owner_id: int = Path(ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    db.delete(owner)
    db.commit()
    return owner


@app.get("/cats", response_model=List[CatResponse], tags=["cats"])
async def get_cats(limit: int = Query(10, le=300), offset: int = 0, db: Session = Depends(get_db)):
    cats = db.query(Cat).limit(limit).offset(offset).all()
    return cats


@app.get("/cats/{cat_id}", response_model=CatResponse, tags=["cats"])
async def get_cat(cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    return cat


@app.post("/cats", response_model=CatResponse, tags=["cats"])
async def create_cat(body: CatModel, db: Session = Depends(get_db)):
    cat = Cat(**body.dict())  # Owner(**body.dict())
    db.add(cat)
    db.commit()
    return cat


@app.put("/cats/{cat_id}", response_model=CatResponse, tags=["cats"])
async def update_cat(body: CatModel, cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    cat.nick = body.nick
    cat.age = body.age
    cat.description = body.description
    cat.vaccinated = body.vaccinated
    cat.owner_id = body.owner_id
    db.commit()
    return cat


@app.delete("/cats/{cat_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["cats"])
async def delete_cat(cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    db.delete(cat)
    db.commit()
    return None


@app.patch("/cats/{cat_id}/vaccinated", response_model=CatResponse, tags=["cats"])
async def vaccinated_cat(body: CatVaccinatedModel, cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found!")
    cat.vaccinated = body.vaccinated
    db.commit()
    return cat
