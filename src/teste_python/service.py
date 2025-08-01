from typing import List
import heapq


class Contract:
    def __init__(self, id: int, debt: float):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


def get_top_N_open_contracts(open_contracts: List[Contract], renegotiated_contracts: List[int], top_n: int) -> list[
                                                                                                                   int] | None:
    """
    Retorna os top_n maiores devedores que NÃO estão na lista de renegociados.
    Usa heapq.nlargest para evitar ordenação completa da lista.
    Ideal para quando top_n << len(open_contracts).

    :param open_contracts: Lista de objetos Contract (com id e debt)
    :param renegotiated_contracts: Lista de ids que já renegociaram
    :param top_n: Quantidade de devedores a retornar
    :return: Lista com os ids dos top_n maiores devedores (não renegociados), ordenados por dívida decrescente
    """
    # Conversão para set: O(m), onde m = len(renegotiated_contracts)
    renegotiated_set = set(renegotiated_contracts)

    # Gerador para filtrar contratos não renegociados
    non_renegotiated = (
        contract for contract in open_contracts
        if contract.id not in renegotiated_set
    )

    # heapq.nlargest: O(n log(top_n)) ~ muito mais rápido que sort() se top_n for pequeno
    top_contracts = heapq.nlargest(top_n, non_renegotiated, key=lambda x: x.debt)

    # Extrai apenas os IDs
    return [contract.id for contract in top_contracts]

    pass

