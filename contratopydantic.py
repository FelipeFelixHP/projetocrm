from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, ValidationError
from datetime import datetime, time
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Camisas Masculinas"
    produto2 = "Camisas Femininas"
    produto3 = "Calças"

class Vendas(BaseModel):
        """
        Modelo de dados para as vendas.

        Args:
            email (EmailStr, verifica se é um email valido, pra fazer essa verificação no db teria que ser feito um stored procedure): email do comprador
            data (datetime): data da compra
            valor (PositiveFloat): valor da compra
            produto (PositiveInt, para garantir que a pessoa não digite exemplo -50 no 
            nome do produto, no python tem esse tipo de dados também, porem tem que importar )
            quantidade (PositiveInt): quantidade de produtos
            produto (ProdutoEnum): categoria do produto
        """
        email: EmailStr
        data: datetime
        valor: PositiveFloat
        quantidade: PositiveInt
        produto: ProdutoEnum
