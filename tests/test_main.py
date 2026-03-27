import pytest
from unittest.mock import patch
from apps.cli_client.main import main

@pytest.fixture
def mock_engine_io():
    """Mocks subprocess and file operations to prevent actual PDF generation/opening in tests."""
    with patch("subprocess.run") as mock_run, \
         patch("mathosynthesis.handlers.files_handler.delete_file"), \
         patch("mathosynthesis.handlers.files_handler.open_file"), \
         patch("mathosynthesis.handlers.files_handler.reveal_file"):
        yield mock_run

@pytest.mark.parametrize(
    "argv, mock_input",
    [
        # Case 1: Using setup_name explicitly
        (["mathos", "--setup", "basic-operations.json"], None),
        # Case 2: Using the number index directly in args
        (["mathos", "-s", "1"], None),
        # Case 3: No arguments, interactive selection (Simulating user typing "1")
        (["mathos"], "1"),
    ]
)
def test_cli_setup_selection(monkeypatch, mock_engine_io, argv, mock_input):
    # Mock sys.argv
    monkeypatch.setattr("sys.argv", argv)
    
    # Mock user input if needed
    if mock_input is not None:
        monkeypatch.setattr("builtins.input", lambda _: mock_input)
    
    # Run the main CLI entry point
    main()

    # Verify that the generation logic (which calls subprocess.run for Pandoc) was triggered
    assert mock_engine_io.called