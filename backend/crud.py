import csv
from sqlalchemy import func
from sqlalchemy.orm import Session
from models import ListingMaster
from schemas import Listing


def create_listing(db: Session, listing: Listing):
    db_listing = ListingMaster(
        business_name=listing.business_name,
        category=listing.category,
        city=listing.city,
        address=listing.address,
        phone=listing.phone,
        source=listing.source
    )

    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)

    return db_listing


def get_listings(db: Session, city=None, category=None):
    query = db.query(ListingMaster)

    if city:
        query = query.filter(ListingMaster.city == city)

    if category:
        query = query.filter(ListingMaster.category == category)

    return query.all()



def city_summary(db: Session):
    return (
        db.query(
            ListingMaster.city,
            func.count(ListingMaster.id).label("count")
        )
        .group_by(ListingMaster.city)
        .all()
    )


def category_summary(db: Session):
    return (
        db.query(
            ListingMaster.category,
            func.count(ListingMaster.id).label("count")
        )
        .group_by(ListingMaster.category)
        .all()
    )


def source_summary(db: Session):
    return (
        db.query(
            ListingMaster.source,
            func.count(ListingMaster.id).label("count")
        )
        .group_by(ListingMaster.source)
        .all()
    )
# -------------------------
# UPDATE
# -------------------------
def update_listing(db: Session, listing_id: int, listing: Listing):
    db_listing = db.query(ListingMaster).filter(
        ListingMaster.id == listing_id
    ).first()

    if not db_listing:
        return None

    db_listing.business_name = listing.business_name
    db_listing.category = listing.category
    db_listing.city = listing.city
    db_listing.address = listing.address
    db_listing.phone = listing.phone
    db_listing.source = listing.source

    db.commit()
    db.refresh(db_listing)

    return db_listing


# -------------------------
# DELETE
# -------------------------
def delete_listing(db: Session, listing_id: int):
    db_listing = db.query(ListingMaster).filter(
        ListingMaster.id == listing_id
    ).first()

    if not db_listing:
        return None

    db.delete(db_listing)
    db.commit()

    return {"message": "Listing Deleted Successfully"}
def bulk_insert(db: Session):
    with open("business_listings.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            listing = ListingMaster(
                business_name=row["business_name"],
                category=row["category"],
                city=row["city"],
                address=row["address"],
                phone=row["phone"],
                source=row["source"]
            )

            db.add(listing)

        db.commit()

    return {"message": "500 Listings Inserted Successfully"}