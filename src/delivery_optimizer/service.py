# src/delivery_optimizer/service.py
"""
Módulo de serviço adicional (ex: integração futura com API, logs, etc).
"""

from .orders import Orders


def calculate_min_trips(requests: list[int], n_max: int) -> int:
    """
    Função helper para facilitar uso direto da lógica.
    """
    return Orders().combine_orders(requests, n_max)