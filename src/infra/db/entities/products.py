import enum
from sqlalchemy import Column, String, BIGINT, Float, Enum
from src.infra.db.settings import Base


class ProductTypes(enum.Enum):
    clothing = "clothing"
    electronic = "electronic"
    food = "food"
    cleaning = "cleaning"


class Products(Base):
    __tablename__ = "products"

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    value = Column(Float, nullable=False)
    product_type = Column(Enum(ProductTypes), nullable=False)
