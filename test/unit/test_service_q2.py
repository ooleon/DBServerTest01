# tests/unit/test_service_q2.py
# tests/unit/test_service.py
"""
Testes unitários para combine_orders.
"""

import pytest
from src.delivery_optimizer.orders import Orders


class TestCombineOrders:
    def test_example_case(self, small_requests, n_max):
        """Caso do enunciado."""
        result = Orders().combine_orders(small_requests, n_max)
        assert result == 2

    def test_single_request(self, single_request, n_max):
        """Um único pedido: uma viagem."""
        result = Orders().combine_orders(single_request, n_max)
        assert result == 1

    def test_two_compatible_requests(self, n_max):
        """Dois pedidos que cabem juntos."""
        result = Orders().combine_orders([50, 50], n_max)
        assert result == 1

    def test_two_incompatible_requests(self, n_max):
        """Dois pedidos que não cabem juntos."""
        result = Orders().combine_orders([60, 50], 100)
        assert result == 2

    def test_empty_requests(self, empty_requests, n_max):
        """Lista vazia: zero viagens."""
        result = Orders().combine_orders(empty_requests, n_max)
        assert result == 0

    def test_all_individual(self, n_max):
        """Todos os pedidos são altos e não podem ser combinados."""
        result = Orders().combine_orders([90, 85, 80], 100)
        assert result == 3

    def test_all_pairs(self, medium_requests, n_max):
        """Vários pares podem ser combinados."""
        result = Orders().combine_orders(medium_requests, n_max)
        # [10,20,30,40,60] → (60+40), (30+20), (10) → 3 viagens?
        # Mas algoritmo: ordena → [10,20,30,40,60]
        # 10+60 ≤ 100 → sim → viagem
        # 20+40 ≤ 100 → sim → viagem
        # 30 → viagem
        # Total: 3
        assert result == 3

    def test_exact_capacity(self, n_max):
        """Combinações exatas com n_max."""
        result = Orders().combine_orders([100, 50, 50], 100)
        # 100 → viagem
        # 50+50 → viagem
        assert result == 2

    def test_max_capacity_requests(self, max_capacity_requests, n_max):
        """Pedidos iguais a n_max ou menores."""
        result = Orders().combine_orders(max_capacity_requests, n_max)
        # [100,100,50,50] → 100 (1 viagem), 100 (1), 50+50 (1) → total 3
        assert result == 3

    def test_large_dataset_performance(self, large_requests, n_max):
        """Testa desempenho com grande volume."""
        import time
        start = time.time()
        result = Orders().combine_orders(large_requests, n_max)
        end = time.time()

        assert result > 0
        assert end - start < 0.1  # Deve ser rápido mesmo com 900 pedidos

    @pytest.mark.parametrize("invalid_value", [-1, 0])
    def test_invalid_n_max_raises_error(self, small_requests, invalid_value):
        """n_max deve ser positivo."""
        with pytest.raises(ValueError):
            Orders().combine_orders(small_requests, invalid_value)

    def test_negative_request_raises_error(self, n_max):
        """Pedidos negativos não são permitidos."""
        with pytest.raises(ValueError):
            Orders().combine_orders([10, -5, 20], n_max)

    def test_zero_request_raises_error(self, n_max):
        """Pedido zero não faz sentido no contexto."""
        with pytest.raises(ValueError):
            Orders().combine_orders([0, 10], n_max)