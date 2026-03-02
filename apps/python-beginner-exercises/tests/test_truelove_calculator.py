import pytest
from src.truelove_calculator import calculate_truelove_score


def test_calculate_truelove_score_basic():
    """Test basic functionality with simple names."""
    # Test case: "Alice" + "Bob"
    # Combined: "ALICEBOB"
    # TRUE letters: A=1, L=1, I=0, E=0, T=0 = 2 (but L appears in both, so actual count is 1)
    # LOVE letters: L=1, O=1, V=0, E=0 = 2 (but L appears in both, so actual count is 3)
    # Let me recalculate properly:
    # ALICEBOB: A=1, L=1, I=1, C=1, E=1, B=1, O=1
    # TRUE letters: T=0, R=0, U=0, E=1 = 1
    # LOVE letters: L=1, O=1, V=0, E=1 = 3
    # Score: 13
    assert calculate_truelove_score("Alice", "Bob") == 13


def test_calculate_truelove_score_case_insensitive():
    """Test that the function is case insensitive."""
    assert calculate_truelove_score("alice", "bob") == calculate_truelove_score("ALICE", "BOB")
    assert calculate_truelove_score("Alice", "Bob") == calculate_truelove_score("ALICE", "BOB")


def test_calculate_truelove_score_true_love():
    """Test with names that contain the actual words."""
    # "True" + "Love"
    # Combined: "TRUELOVE"
    # TRUE letters: T=1, R=1, U=1, E=2 = 5
    # LOVE letters: L=1, O=1, V=1, E=2 = 5 (E is counted twice)
    # Score: 55
    assert calculate_truelove_score("True", "Love") == 55


def test_calculate_truelove_score_empty_names():
    """Test with empty names."""
    assert calculate_truelove_score("", "") == 0


def test_calculate_truelove_score_single_names():
    """Test with single letter names."""
    # "T" + "L"
    # Combined: "TL"
    # TRUE letters: T=1, R=0, U=0, E=0 = 1
    # LOVE letters: L=1, O=0, V=0, E=0 = 1
    # Score: 11
    assert calculate_truelove_score("T", "L") == 11


def test_calculate_truelove_score_repeated_letters():
    """Test with names containing repeated letters."""
    # "Tutor" + "Eve"
    # Combined: "TUTOREVE"
    # TRUE letters: T=2, R=1, U=1, E=2 = 6
    # LOVE letters: L=0, O=1, V=1, E=2 = 4
    # Score: 64
    assert calculate_truelove_score("Tutor", "Eve") == 64


def test_calculate_truelove_score_no_matching_letters():
    """Test with names that have no matching letters."""
    # "XYZ" + "ABC"
    # Combined: "XYZABC"
    # TRUE letters: T=0, R=0, U=0, E=0 = 0
    # LOVE letters: L=0, O=0, V=0, E=0 = 0
    # Score: 0
    assert calculate_truelove_score("XYZ", "ABC") == 0


def test_calculate_truelove_score_high_score():
    """Test with names that should give a high score."""
    # "Eternity" + "Revolution"
    # Combined: "ETERNITYREVOLUTION"
    # TRUE letters: T=3, R=3, U=1, E=4 = 11
    # LOVE letters: L=1, O=2, V=2, E=4 = 9
    # Score: 119 (but since we want a 2-digit score, this would be 119)
    # Let's test with a simpler case
    assert calculate_truelove_score("Eternal", "Love") > 50
