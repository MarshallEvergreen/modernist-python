"""Create an engine for the orm."""

import os

from sqlalchemy import Engine, create_engine


def create_postgres_engine() -> Engine:
    """Create a PostgreSQL engine.

    Configure however you see fit to be able to pass the actual
    production database URL in a secure manner.
    """
    url = os.getenv(
        "DATABASE_URL", "postgresql+psycopg://dba:password@localhost:5432/modernist"
    )
    return create_engine(url)
