from src.teste_python.service import  *

if __name__ == "__main__":
    contracts = [
        Contract(1, 1.1),
        Contract(2, 2.65),
        Contract(3, 3.78),
        Contract(4, 4.89),
        Contract(6, 6.89),
        Contract(40, 4.89),
        Contract(41, 4.9),
        Contract(42, 4.7),
        Contract(43, 4.89),
        Contract(44, 4.89),
        Contract(45, 4.89),
        Contract(48, 40.89),
        Contract(5, 5.78)
    ]
    renegotiated = [3,4]
    top_n = 6

    actual_open_contracts = get_top_N_open_contracts(contracts, renegotiated, top_n)
    expected_open_contracts = [48, 6, 5, 41, 40, 43]
    assert expected_open_contracts == actual_open_contracts
    print("✅ actual_open_contracts ", actual_open_contracts)




