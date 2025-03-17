import databases
import sqlalchemy
import os

metadata = sqlalchemy.MetaData()

user_table = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("middle_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("password", sqlalchemy.String)
)

todo_table = sqlalchemy.Table(
    "todo",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("task", sqlalchemy.String),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("user.id"), nullable=False),
    sqlalchemy.Column("Date", sqlalchemy.DateTime, server_default=sqlalchemy.func.now())
)

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError(" DATABASE_URL is not set or is not accessible!")

database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)

async def connect_db():
    """Connect to the database on startup."""
    await database.connect()

async def disconnect_db():
    """Disconnect from the database on shutdown."""
    await database.disconnect()

def create_tables():
    """Create the tables in the database if they do not exist"""
    metadata.create_all(engine)
    print("created successfully ✅")

