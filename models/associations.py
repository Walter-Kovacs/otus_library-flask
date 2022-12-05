from sqlalchemy import (
    Column,
    ForeignKey,
    Table,
)

from .database import db


books_authors = Table(
    "books_authors",
    db.metadata,
    Column("author_id", ForeignKey("book.id")),
    Column("book_id", ForeignKey("author.id")),
)
