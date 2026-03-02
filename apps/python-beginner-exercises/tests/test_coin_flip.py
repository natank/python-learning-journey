import pytest
from src.coin_flip import flip_coin, flip_multiple_times

def test_flip_coin():
    result = flip_coin()
    assert result in ['Heads', 'Tails']

def test_flip_multiple_times():
    results = flip_multiple_times(10)
    assert len(results) == 10
    for result in results:
        assert result in ['Heads', 'Tails']
    
    # Should have at least one of each (very likely with 10 flips)
    assert 'Heads' in results or 'Tails' in results

def test_flip_multiple_times_zero():
    results = flip_multiple_times(0)
    assert results == []

def test_flip_multiple_times_one():
    results = flip_multiple_times(1)
    assert len(results) == 1
    assert results[0] in ['Heads', 'Tails']
