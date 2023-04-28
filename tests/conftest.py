import pytest


@pytest.fixture
def source_1():
    return {
        "Rapid Wien - First Vienna": {"id": "RapidWien_FirstVienna", "w1": 1.93, "x": 2.32, "w2": 7.44},
        "Al Bourj - Al Nejmeh": {"id": "Bourj_Nejmeh", "w1": 26, "x": 11.5, "w2": 1.05},
    }


@pytest.fixture
def source_2():
    return {
        "Bourj FC - Nejmeh SC Beirut": {"id": "Bourj_Nejmeh", "w1": 32, "x": 12, "w2": 1.05},
        "SK Rapid Wien - First Vienna FC": {"id": "RapidWien_FirstVienna", "w1": 1.97, "x": 2.3, "w2": 8.2},
    }
