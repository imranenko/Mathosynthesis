import pytest
from mathosynthesis.main import main


@pytest.mark.parametrize(
    "argv",
    [
        ["prog", "--setup", "basic_operations.json"],
        ["prog", "--setup", "basic_operations.json", "--open", "True"],
        ["prog", "--setup", "basic_operations.json", "--reveal", "True"],
        ["prog", "--setup", "basic_operations.json", "--markdown", "True"],
    ]
)
def test_main(monkeypatch, argv):
    monkeypatch.setattr("sys.argv", argv)
    main()