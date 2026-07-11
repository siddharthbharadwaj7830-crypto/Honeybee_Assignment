from pydantic import BaseModel


class Listing(BaseModel):
    business_name: str
    category: str
    city: str
    address: str
    phone: str
    source: str


class DashboardResponse(BaseModel):
    name: str
    count: int