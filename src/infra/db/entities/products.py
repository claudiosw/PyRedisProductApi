from sqlalchemy import Column, String, BIGINT, Numeric, Enum
from src.infra.db.settings import Base
from .product_types import ProductTypes


class Products(Base):
    __tablename__ = "products"

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    value = Column(Numeric, nullable=False)
    product_type = Column(Enum(ProductTypes), nullable=False)
