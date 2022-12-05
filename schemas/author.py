from pydantic import BaseModel, constr


class Author(BaseModel):
    name: constr(min_length=1, max_length=100)
    description: str
