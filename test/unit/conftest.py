# tests/conftest.py
import pytest
from src.teste_python.service import Contract, get_top_N_open_contracts

# Fixtures para Question 1
@pytest.fixture
def sample_contracts():
    """Retorna uma lista de contratos de exemplo."""
    return [
        Contract(1, 100),
        Contract(2, 200),
        Contract(3, 150),
    ]

@pytest.fixture
def renegotiated_ids():
    """Retorna uma lista de IDs renegociados (ex: ID 2 e 5)."""
    return [2]

@pytest.fixture
def empty_contract_list():
    """Lista vazia de contratos."""
    return []


# Fixtures para Question 2
@pytest.fixture
def small_requests():
    return [70, 30, 10]


@pytest.fixture
def medium_requests():
    return [60, 40, 30, 20, 10]


@pytest.fixture
def large_requests():
    return [90, 80, 70, 60, 50, 40, 30, 20, 10] * 10  # 90 pedidos


@pytest.fixture
def n_max():
    return 100


@pytest.fixture
def single_request():
    return [50]


@pytest.fixture
def empty_requests():
    return []


@pytest.fixture
def max_capacity_requests():
    return [100, 100, 50, 50]