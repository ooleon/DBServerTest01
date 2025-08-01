# tests/unit/test_service_q1.py

import pytest
from src.teste_python.service import get_top_N_open_contracts


def test_top_n_debtors_excluding_renegotiated(sample_contracts, renegotiated_ids):
    result = get_top_N_open_contracts(sample_contracts, renegotiated_ids, top_n=2)
    assert result == [3, 1]  # Contract 2 foi renegociado

def test_top_2_from_small_set(small_contract_set, renegotiated_small):
    result = get_top_N_open_contracts(small_contract_set, renegotiated_small, top_n=2)
    assert result == [4, 3]  # IDs dos maiores devedores não renegociados


def test_large_set_performance(large_contract_set, renegotiated_large):
    result = get_top_N_open_contracts(large_contract_set, renegotiated_large, top_n=5)
    assert len(result) == 5
    assert result[0] == 1000  # Maior devedor não renegociado


def test_ties_preserve_order(contracts_with_ties, no_renegotiated):
    result = get_top_N_open_contracts(contracts_with_ties, no_renegotiated, top_n=2)
    # Como dívidas são iguais, heapq mantém ordem de aparição
    assert result == [40, 50]  # Os dois primeiros com 200


def test_zero_debt_excluded_when_needed(contracts_with_zero_debt, no_renegotiated):
    result = get_top_N_open_contracts(contracts_with_zero_debt, no_renegotiated, top_n=3)
    # Contratos com dívida 0 são válidos, mas têm prioridade baixa
    assert result == [2, 4, 1]  # 2 (100), 4 (50), 1 (0) — ID 3 também 0, mas vem depois


def test_empty_returns_empty(empty_contract_set, no_renegotiated):
    result = get_top_N_open_contracts(empty_contract_set, no_renegotiated, top_n=3)
    assert result == []


def test_all_renegotiated_returns_empty(small_contract_set, all_renegotiated):
    # Forçamos todos como renegociados (mesmo que não batam 1:1, só para teste)
    over_renegotiated = [c.id for c in small_contract_set]
    result = get_top_N_open_contracts(small_contract_set, over_renegotiated, top_n=3)
    assert result == []


# ✅ Teste parametrizado: roda em múltiplos cenários
@pytest.mark.parametrize("any_small_dataset", [
    "small_contract_set",
    "contracts_with_ties",
    "contracts_with_zero_debt"
], indirect=True)
def test_top_1_in_various_scenarios(any_small_dataset, no_renegotiated):
    result = get_top_N_open_contracts(any_small_dataset, no_renegotiated, top_n=1)
    assert len(result) == 1
    # Apenas verifica que retorna 1 ID válido
    assert isinstance(result[0], int)