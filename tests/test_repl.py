from unittest.mock import patch
from calculator.repl import parse_number, start_repl


def test_parse_number():
    with patch("builtins.input", return_value="42"):
        assert parse_number("Prompt: ") == 42.0


def test_parse_number_invalid_retry():
    with patch("builtins.input", side_effect=["invalid", "10"]):
        assert parse_number("Prompt: ") == 10.0


def test_repl_full_loop():
    inputs = ["add", "10", "15", "invalid_op", "divide", "10", "0", "exit"]
    with patch("builtins.input", side_effect=inputs):
        start_repl()
