# tests/unit/test_service_q1.py
from src.teste_python.service import get_top_N_open_contracts


def test_top_n_debtors_excluding_renegotiated(sample_contracts, renegotiated_ids):
    result = get_top_N_open_contracts(sample_contracts, renegotiated_ids, top_n=2)
    assert result == [3, 1]  # Contract 2 foi renegociado
