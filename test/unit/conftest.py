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


@pytest.fixture
def small_contract_set():
    """Cenário pequeno: 5 contratos, ideal para testes unitários rápidos."""
    return [
        Contract(1, 100),
        Contract(2, 200),
        Contract(3, 150),
        Contract(4, 300),
        Contract(5, 50),
    ]


@pytest.fixture
def large_contract_set():
    """Cenário grande: 1000 contratos, para testar performance e escala."""
    return [Contract(i, i * 10) for i in range(1, 1001)]


@pytest.fixture
def contracts_with_ties():
    """Cenário com dívidas iguais: testa estabilidade da ordenação."""
    return [
        Contract(10, 100),
        Contract(20, 100),
        Contract(30, 100),
        Contract(40, 200),
        Contract(50, 200),
    ]


@pytest.fixture
def contracts_with_zero_debt():
    """Cenário com dívidas zero: verifica se são tratados corretamente."""
    return [
        Contract(1, 0),
        Contract(2, 100),
        Contract(3, 0),
        Contract(4, 50),
    ]


@pytest.fixture
def empty_contract_set():
    """Cenário vazio: para testar limites."""
    return []


# ========================================
# 🔄 Fixtures: Listas de renegociações
# ========================================

@pytest.fixture
def renegotiated_small():
    """Alguns IDs renegociados no conjunto pequeno."""
    return [2, 5]


@pytest.fixture
def renegotiated_large():
    """Múltiplos IDs renegociados (múltiplos de 7) no conjunto grande."""
    return [i for i in range(1, 1001) if i % 7 == 0]


@pytest.fixture
def no_renegotiated():
    """Nenhum contrato renegociado."""
    return []


@pytest.fixture
def all_renegotiated():
    """Todos os IDs possíveis renegociados (para teste de retorno vazio)."""
    return list(range(1, 1001))


# ========================================
# 🧪 Fixtures Compostas (cenários completos)
# ========================================

@pytest.fixture
def scenario_basic():
    """Cenário básico: pequeno + alguns renegociados."""
    return {
        "contracts": [
            Contract(1, 100),
            Contract(2, 200),
            Contract(3, 150),
            Contract(4, 300),
            Contract(5, 50),
        ],
        "renegotiated": [2],
        "expected_top_2": [4, 3],
    }


@pytest.fixture
def scenario_ties():
    """Cenário com empates em dívida."""
    return {
        "contracts": [
            Contract(1, 100),
            Contract(2, 100),
            Contract(3, 100),
        ],
        "renegotiated": [2],
        "expected_top_2": [1, 3],
    }


# Parametrização Avançada (opcional)
@pytest.fixture(params=[
    "small_contract_set",
    "contracts_with_ties",
    "contracts_with_zero_debt"
])
def any_small_dataset(request):
    """
    Fixture parametrizada: executa o teste com múltiplos conjuntos pequenos.
    Use com @pytest.mark.parametrize para testar em todos.
    """
    return request.getfixturevalue(request.param)

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