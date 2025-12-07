import pytest
from unittest.mock import patch
from mathosynthesis.handlers import cli_handler

@pytest.mark.parametrize(
    "argv, expected",
    [
        (["prog"], {"setup": None, "open": None, "reveal": None, "markdown": None, "language": None}),
        (["prog", "--setup", "setup.json"], {"setup": "setup.json"}),
        (["prog", "--open"], {"open": True}),
        (["prog", "--open", "false"], {"open": False}),
        (["prog", "--reveal", "yes"], {"reveal": True}),
        (["prog", "--markdown", "0"], {"markdown": False}),
        (["prog", "--language", "en", "de"], {"language": ["en", "de"]}),
    ]
)
def test_parse_args_various(monkeypatch, argv, expected):
    monkeypatch.setattr("sys.argv", argv)
    args = cli_handler.parse_args()
    for key, val in expected.items():
        assert getattr(args, key) == val

def test_build_printable_setups_formats_correctly():
    setups = {
        "Algebra": ["alg1.json", "alg2.json"],
        "NO_CATEGORY": ["no_cat1.json"]
    }
    lines = cli_handler.build_printable_setups(setups)
    assert any("=== SETUPS ===" in line for line in lines)
    assert any("Algebra" in line for line in lines)
    assert any("1." in line and "alg1.json" in line for line in lines)

@patch("builtins.input", side_effect=["invalid", "5", "1"])
def test_ask_setup_handles_invalid_and_valid_input(mock_input):
    setups = {
        "Category1": ["file1.json", "file2.json"],
        "NO_CATEGORY": ["file3.json"]
    }
    path = cli_handler.ask_setup(setups)
    assert path.endswith("Category1/file1.json")

def test_str_to_bool_accepts_various_inputs():
    true_vals = ["true", "1", "yes", "y", "True"]
    false_vals = ["false", "0", "no", "n", "False"]

    for val in true_vals:
        assert cli_handler._str_to_bool(val) is True
    for val in false_vals:
        assert cli_handler._str_to_bool(val) is False

    import argparse
    with pytest.raises(argparse.ArgumentTypeError):
        cli_handler._str_to_bool("notabool")