from sqlalchemy.orm import Session

from models import Author
from schemas import Author as AuthorSchema


# ***************************** CREATE *****************************
def create_author(session: Session, author_schema: AuthorSchema) -> Author:
    author: Author = Author(**author_schema.dict())
    session.add(author)
    session.commit()

    return author

# ***************************** READ *****************************
# ***************************** UPDATE *****************************
# ***************************** DELETE *****************************
