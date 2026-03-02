import pytest
from src.caesar_cipher import caesar_encoder, caesar_decoder


class TestCaesarEncoder:
    """Test cases for Caesar cipher encoder function."""
    
    def test_basic_encoding(self):
        """Test basic encoding with simple text."""
        assert caesar_encoder("hello", 3) == "khoor"
        assert caesar_encoder("abc", 1) == "bcd"
        assert caesar_encoder("xyz", 2) == "zab"
    
    def test_uppercase_preservation(self):
        """Test that uppercase letters remain uppercase."""
        assert caesar_encoder("HELLO", 3) == "KHOOR"
        assert caesar_encoder("Hello", 3) == "Khoor"
        assert caesar_encoder("AbC", 1) == "BcD"
    
    def test_wrap_around(self):
        """Test wrapping from z to a."""
        assert caesar_encoder("xyz", 3) == "abc"
        assert caesar_encoder("XYZ", 3) == "ABC"
        assert caesar_encoder("z", 1) == "a"
        assert caesar_encoder("Z", 1) == "A"
    
    def test_non_alpha_characters(self):
        """Test that non-alphabetic characters remain unchanged."""
        assert caesar_encoder("hello world!", 3) == "khoor zruog!"
        assert caesar_encoder("123", 5) == "123"
        assert caesar_encoder("hello@123", 2) == "jgnnq@123"
        assert caesar_encoder(" ", 10) == " "
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        assert caesar_encoder("", 5) == ""
        assert caesar_encoder("a", 25) == "z"
        assert caesar_encoder("z", 25) == "y"
        assert caesar_encoder("A", 25) == "Z"
        assert caesar_encoder("Z", 25) == "Y"
    
    def test_max_shift(self):
        """Test maximum shift value."""
        assert caesar_encoder("hello", 25) == "gdkkn"
        assert caesar_encoder("abc", 25) == "zab"


class TestCaesarDecoder:
    """Test cases for Caesar cipher decoder function."""
    
    def test_basic_decoding(self):
        """Test basic decoding with simple text."""
        assert caesar_decoder("khoor", 3) == "hello"
        assert caesar_decoder("bcd", 1) == "abc"
        assert caesar_decoder("zab", 2) == "xyz"
    
    def test_uppercase_preservation(self):
        """Test that uppercase letters remain uppercase."""
        assert caesar_decoder("KHOOR", 3) == "HELLO"
        assert caesar_decoder("Khoor", 3) == "Hello"
        assert caesar_decoder("BcD", 1) == "AbC"
    
    def test_wrap_around(self):
        """Test wrapping from a to z."""
        assert caesar_decoder("abc", 3) == "xyz"
        assert caesar_decoder("ABC", 3) == "XYZ"
        assert caesar_decoder("a", 1) == "z"
        assert caesar_decoder("A", 1) == "Z"
    
    def test_non_alpha_characters(self):
        """Test that non-alphabetic characters remain unchanged."""
        assert caesar_decoder("khoor zruog!", 3) == "hello world!"
        assert caesar_decoder("123", 5) == "123"
        assert caesar_decoder("jgnnq@123", 2) == "hello@123"
        assert caesar_decoder(" ", 10) == " "
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        assert caesar_decoder("", 5) == ""
        assert caesar_decoder("z", 25) == "a"
        assert caesar_decoder("y", 25) == "z"
        assert caesar_decoder("Z", 25) == "A"
        assert caesar_decoder("Y", 25) == "Z"
    
    def test_max_shift(self):
        """Test maximum shift value."""
        assert caesar_decoder("gdkkn", 25) == "hello"
        assert caesar_decoder("zab", 25) == "abc"


class TestEncoderDecoderIntegration:
    """Test cases for encoder-decoder integration."""
    
    def test_round_trip(self):
        """Test that encoding and decoding returns original text."""
        original = "Hello World! 123"
        for shift in range(1, 26):
            encoded = caesar_encoder(original, shift)
            decoded = caesar_decoder(encoded, shift)
            assert decoded == original
    
    def test_different_shifts(self):
        """Test with various shift amounts."""
        test_cases = [
            ("hello", 1, "ifmmp"),
            ("hello", 5, "mjqqt"),
            ("hello", 10, "rovvy"),
            ("hello", 20, "byffi"),
            ("HELLO WORLD", 13, "URYYB JBEYQ"),
        ]
        
        for original, shift, expected in test_cases:
            assert caesar_encoder(original, shift) == expected
            assert caesar_decoder(expected, shift) == original
    
    def test_mixed_content(self):
        """Test with mixed content including numbers and symbols."""
        original = "The quick brown fox jumps over 13 lazy dogs!"
        shift = 7
        encoded = caesar_encoder(original, shift)
        decoded = caesar_decoder(encoded, shift)
        
        assert decoded == original
        assert encoded != original  # Ensure encoding actually changed the text
