import uuid

from dateutil.relativedelta import relativedelta

from .model import Transaction


def create_transaction_logic(data):
    if data.installments > 1:
        # Lógica de Parcelamento
        valor_parcela = data.amount / data.installments
        group_id = uuid.uuid4()  # Identidade do grupo

        lista_transacoes = []

        for i in range(data.installments):
            # Calcular a data correta para cada mês
            # Cuidado: Somar 30 dias não funciona (Fevereiro tem 28).
            # Use uma lib como 'dateutil.relativedelta'
            data_parcela = data.date + relativedelta(months=+i)

            # Ajuste Fino: Se for Cartão de Crédito, tem que ver o dia de fechamento!
            # Se comprou dia 20 e fecha dia 15 -> Cai no próximo mês.
            # Se comprou dia 10 e fecha dia 15 -> Cai neste mês.

    #         nova_transacao = Transaction(
    #             description=f"{data.description} ({i+1}/{data.installments})",
    #             amount=valor_parcela,
    #             date=data_parcela,
    #             installment_number=i+1,
    #             total_installments=data.installments,
    #             transaction_group_id=group_id,
    #             # ... outros campos ...
    #         )
    #         lista_transacoes.append(nova_transacao)

    #     session.add_all(lista_transacoes)

    # else:
    #     # Lógica Simples (A vista)
    #     session.add(Transaction(...))
