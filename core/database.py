from sqlmodel import SQLModel, create_engine, Session
import logging

# Set up logging for better debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./sports_club.db"

# Create the database engine
try:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    logger.info("Database engine created successfully.")
except Exception as e:
    logger.error(f"Error creating database engine: {e}")
    raise

# Function to create database tables
def create_db_tables():
    try:
        logger.info("Creating database tables...")
        SQLModel.metadata.create_all(engine)
        logger.info("Database tables created successfully.")
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        raise

# Dependency to get the database session
def get_db():
    try:
        logger.info("Opening database session...")
        with Session(engine) as session:
            yield session
            logger.info("Database session closed.")
    except Exception as e:
        logger.error(f"Error with database session: {e}")
        raise
