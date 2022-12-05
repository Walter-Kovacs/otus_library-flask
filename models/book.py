from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from .associations import books_authors
from .database import db


class Book(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(
        String(200),
        nullable=False,
    )
    abstract = Column(Text)
    count = Column(
        Integer,
        nullable=False,
        default=0,
        server_default="0",
    )

    authors = relationship("Author", secondary=books_authors, back_populates="books")
