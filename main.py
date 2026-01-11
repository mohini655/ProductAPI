from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from config import session_local, engine
from models import Product
import database_models
app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greeting(name: str = "User"):
    return {f"Hello, {name}!"}

products = [
    Product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=1),
    Product(id=5, name="Smartphone", description="A latest model smartphone", price=699.99, quantity=2),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=5)
]

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = next(get_db())
    count = db.query(database_models.Product).count()
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()

init_db()

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products_db = db.query(database_models.Product).all()
    return products_db

@app.get("/product/{product_id}")
def get_product(product_id: int, db:Session = Depends(get_db)):
    product = db.query(database_models.Product).filter_by(id = product_id).all()
    if product:
        return product
    return {"error": "Product not found"}


@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return {"message": "Product added successfully"}


@app.put("/product/{product_id}")
def update_product(product_id: int, new_product: Product, db: Session = Depends(get_db)):
    res_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if res_product:
        res_product.name = new_product.name
        res_product.description = new_product.description
        res_product.price = new_product.price
        res_product.quantity = new_product.quantity
        db.commit()
        return {"message": "Product updated successfully"}
    return {"error": "Product not found"}


@app.delete("/product/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    res_product = db.query(database_models.Product).filter(database_models.Product.id == product_id).first()
    if res_product:
        db.delete(res_product)
        db.commit()
        return {"message": "Product deleted successfully"}

    return {"error": "Product not found"}
