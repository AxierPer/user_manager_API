from database.sessions import engine, Base
from database.models import User

Base.metadata.create_all(bind=engine)