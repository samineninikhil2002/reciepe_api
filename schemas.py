from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RecipeBase(BaseModel):
    title: str
    ingredients: str
    instructions: str
    image: Optional[str] = None

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    createdAt: datetime
    updatedAt: Optional[datetime] = None

    class Config:
        orm_mode = True
