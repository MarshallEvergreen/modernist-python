"""Create an engine for the orm."""

from sqlalchemy import create_engine


def create_postgres_engine():
    """Create a PostgreSQL engine.

    Configure however you see fit to be able to pass the actual
    production database URL in a secure manner.
    """
    return create_engine("postgresql+psycopg://dba:password@localhost:5432/modernist")
