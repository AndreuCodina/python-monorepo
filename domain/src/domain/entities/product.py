from decimal import Decimal

from pydantic import Field

from common.business_error import BusinessError
from domain.entity import Entity


class Product(Entity):
    name: str = Field(min_length=5, max_length=100)
    description: str | None = None
    price: Decimal = Field(gt=Decimal("0.0"))
    is_discontinued: bool
    discontinuation_reason: str | None = None

    @staticmethod
    def publish(name: str, price: Decimal, description: str | None = None) -> "Product":
        return Product(
            name=name, price=price, description=description, is_discontinued=False
        )

    def discontinue(self, discontinuation_reason: str | None = None) -> None:
        if self.is_discontinued:
            error_message = "The product is already discontinued"
            raise BusinessError(error_message)

        self.is_discontinued = True
        self.discontinuation_reason = discontinuation_reason
