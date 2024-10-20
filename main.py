from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas, database

app = FastAPI()

# Initialize the database
database.init_db()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all recipes
@app.get("/recipes", response_model=list[schemas.Recipe])
def read_recipes(db: Session = Depends(get_db)):
    return crud.get_recipes(db)

# POST a new recipe
@app.post("/recipes", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.create_recipe(db, recipe)
