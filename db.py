
import os
# from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("No DATABASE_URL found in environment variables")

# host = 'localhost'
# port = 5432
# dbname = 'mani_test'
# user = 'postgres'
# password = 'Manibabu@2710'
# sslmode = "prefer"
# # clientSecret = ""
# # clientID = ""
# # tenantID = ""
# user_enc = quote_plus(user)
# password_enc =quote_plus(password)

# conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
# DATABASE_URL= f"postgresql://{user_enc}:{password_enc}@{host}/{dbname}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()