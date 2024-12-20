from b3_parser.core.position.calculator.update_strategy.abstract_position_strategy import BasePositionStrategy, \
    PositionMapping
from b3_parser.core.transaction.model.transaction_model import TransactionModel


class LeilaoDeFracaoPositionStrategy(BasePositionStrategy):
    """
    Estratégia para 'leilão de fração'.
    Subtrai a quantidade e ajusta o preço total de acordo.
    """
    def apply(self, trx: TransactionModel, qtd: float, total_price: float) -> PositionMapping:
        qtd -= trx.qtd
        total_price += trx.total_price
        return PositionMapping(qtd=qtd, total_price=total_price)