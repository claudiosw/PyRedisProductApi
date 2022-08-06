from decimal import Decimal
from src.domain.models.products import Products
from src.infra.db.entities.product_types import ProductTypes
from sqlalchemy.orm.exc import NoResultFound
from src.infra.db.settings import db_connection_handler
from src.infra.db.entities.products import Products as ProductsModel
from src.data.interfaces.products_repository import ProductsRepositoryInterface


class ProductsRepository(ProductsRepositoryInterface):

    @classmethod
    def get_product_by_id(self, id: int) -> Products:
        with db_connection_handler as database:
            try:
                product = (
                    database.session
                    .query(ProductsModel)
                    .filter(ProductsModel.id == id)
                    .one()
                )
                return product
            except NoResultFound:
                return None
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def register_product(self, id: int, name: str, value: Decimal, product_type: ProductTypes):

        with db_connection_handler as database:
            try:
                new_product = ProductsModel(id=id, name=name, value=value, product_type=product_type)
                database.session.add(new_product)
                database.session.commit()

                return ProductsModel(
                    id=new_product.id,
                    name=new_product.name,
                    value=new_product.value,
                    product_type=new_product.product_type
                )
            except:
                database.session.rollback()
                raise
            finally:
                database.session.close()

        return None
