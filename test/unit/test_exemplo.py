from src.teste_python.service import Contract, get_top_N_open_contracts

contracts = [
    Contract(1, 1),
    Contract(2, 2),
    Contract(3, 3),
    Contract(4, 4),
    Contract(5, 5)
]
renegotiated = [3]
top_n = 3

actual_open_contracts = get_top_N_open_contracts(contracts, renegotiated, top_n)

expected_open_contracts = [5, 4, 2]
assert expected_open_contracts == actual_open_contracts
