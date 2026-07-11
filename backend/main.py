from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
import models
import schemas

from database import SessionLocal, engine

# Create Tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Honeybee Business Listings API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Honeybee Assignment API Running 🚀"}


# ==========================
# LISTING APIs
# ==========================

@app.post("/listings")
def add_listing(listing: schemas.Listing, db: Session = Depends(get_db)):
    return crud.create_listing(db, listing)


from typing import Optional

@app.get("/listings")
def get_all_listings(
    city: Optional[str] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return crud.get_listings(db, city, category)


# ==========================
# DASHBOARD APIs
# ==========================

@app.get("/dashboard/city")
def dashboard_city(db: Session = Depends(get_db)):
    data = crud.city_summary(db)
    return [
        {
            "name": row.city,
            "count": row.count
        }
        for row in data
    ]


@app.get("/dashboard/category")
def dashboard_category(db: Session = Depends(get_db)):
    data = crud.category_summary(db)
    return [
        {
            "name": row.category,
            "count": row.count
        }
        for row in data
    ]


@app.get("/dashboard/source")
def dashboard_source(db: Session = Depends(get_db)):
    data = crud.source_summary(db)
    return [
        {
            "name": row.source,
            "count": row.count
        }
        for row in data
    ]
# ==========================
# UPDATE API
# ==========================

@app.put("/listings/{listing_id}")
def update_listing(
    listing_id: int,
    listing: schemas.Listing,
    db: Session = Depends(get_db)
):
    return crud.update_listing(db, listing_id, listing)


# ==========================
# DELETE API
# ==========================

@app.delete("/listings/{listing_id}")
def delete_listing(
    listing_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_listing(db, listing_id)
# ==========================
# BULK INSERT API
# ==========================

@app.post("/bulk-insert")
def bulk_insert(db: Session = Depends(get_db)):
    return crud.bulk_insert(db)