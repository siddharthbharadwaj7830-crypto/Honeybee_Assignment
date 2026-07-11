from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# MySQL Connection URL
DATABASE_URL = "mysql+pymysql://root:Sidd2007_Honey2026@localhost:3306/honeybee_db"

# Create Engine
engine = create_engine(DATABASE_URL)

# Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base Class
Base = declarative_base()