# src/delivery_optimizer/orders.py
"""
Classe principal que encapsula a lógica de otimização de pedidos.
"""


class Orders:
    """
    Classe responsável por calcular o número mínimo de viagens
    para entregar pedidos de agências, combinando até 2 pedidos por viagem,
    respeitando um valor máximo por entrega.
    """

    def combine_orders(self, requests: list[int], n_max: int) -> int:
        """
        Calcula o número mínimo de viagens para atender todas as requisições.
        Cada viagem pode levar até 2 pedidos, desde que a soma não exceda `n_max`.
        A estratégia é otimizar ao máximo o uso de cada viagem.
        Args:
            requests (List[int]): Lista de valores solicitados pelas agências.
            n_max (int): Valor máximo permitido por viagem.
        Returns: int: Número mínimo de viagens necessárias.
        Examples:
            >>> Orders().combine_orders([70, 30, 10], 100)
            2
            >>> Orders().combine_orders([100, 100], 100)
            2
            >>> Orders().combine_orders([50, 50], 100)
            1
        """
        if not requests:
            return 0
        if any(r <= 0 for r in requests):
            raise ValueError("Todos os pedidos devem ser valores positivos.")
        if n_max <= 0:
            raise ValueError("n_max deve ser maior que zero.")

        # Ordena para aplicar greedy: combinar menor com maior possível
        sorted_requests = sorted(requests)

        left = 0
        right = len(sorted_requests) - 1
        trips = 0

        while left <= right:
            # Tenta combinar o menor e o maior restante
            if left < right and sorted_requests[left] + sorted_requests[right] <= n_max:
                left += 1  # usa o menor com o maior
            # O maior (ou a combinação) consome uma viagem
            right -= 1
            trips += 1

        return trips