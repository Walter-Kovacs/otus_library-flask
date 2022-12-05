from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from .associations import books_authors
from .database import db


class Author(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(
        String(100),
        unique=True,
        nullable=False,
    )
    description = Column(Text)

    books = relationship("Book", secondary=books_authors, back_populates="authors")
