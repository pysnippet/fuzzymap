from fuzzymap import FuzzyMap


def test_basic_usage_1(source_1, source_2):
    """Mapping in source_2 using source_1 keys."""
    source_2 = FuzzyMap(source_2)
    for game, odds in source_1.items():
        assert source_2[game].get("id") == odds.get("id")


def test_basic_usage_2(source_1, source_2):
    """Mapping in source_1 using source_2 keys."""
    source_1 = FuzzyMap(source_1)
    for game, odds in source_2.items():
        assert source_1[game].get("id") == odds.get("id")


def test_not_matching_key_case(source_1):
    """It should not match a key that does not satisfy the ratio."""
    source_1 = FuzzyMap(source_1)
    assert source_1["Some Dummy Key"] is None


def test_with_a_custom_ratio(source_1):
    """A dummy key should match for a small ratio."""
    source_1 = FuzzyMap(source_1)
    source_1.ratio = 24  # decreasing the ratio
    assert source_1["Some Dummy Key"] is not None
