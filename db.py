
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from urllib.parse import quote_plus



host = 'localhost'
port = 5432
dbname = 'mani_test'
user = 'postgres'
password = 'Manibabu@2710'
sslmode = "prefer"
# clientSecret = ""
# clientID = ""
# tenantID = ""
user_enc = quote_plus(user)
password_enc =quote_plus(password)

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
dblink = f"postgresql://{user_enc}:{password_enc}@{host}/{dbname}"

engine = create_engine(dblink)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()