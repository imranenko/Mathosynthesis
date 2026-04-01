import pytest
from unittest.mock import patch, MagicMock
from apps.cli_client.main import main
from pathlib import Path

@pytest.fixture
def mock_cli_deps():
    """Mocks core engine and file operations for CLI testing."""
    with patch("apps.cli_client.main.generate_files", return_value=(Path("dummy.tex"), Path("dummy.pdf"))) as mock_gen, \
         patch("apps.cli_client.main.delete_file") as mock_del, \
         patch("apps.cli_client.main.open_file") as mock_open, \
         patch("apps.cli_client.main.reveal_file") as mock_reveal, \
         patch("apps.cli_client.main.get_setup_path_by_name", return_value=Path("dummy.json")) as mock_path_name, \
         patch("apps.cli_client.main.get_setup_path_by_number", return_value=Path("dummy.json")) as mock_path_num:
        
        yield {
            "generate": mock_gen,
            "delete": mock_del,
            "open": mock_open,
            "reveal": mock_reveal,
            "path_name": mock_path_name,
            "path_num": mock_path_num
        }

def test_cli_setup_arguments(monkeypatch, mock_cli_deps):
    # Setup by name
    monkeypatch.setattr("sys.argv", ["mathos", "--setup", "basic-operations.json"])
    main()
    mock_cli_deps["path_name"].assert_called_once_with("basic-operations.json")
    
    mock_cli_deps["path_name"].reset_mock()
    
    # Setup by number
    monkeypatch.setattr("sys.argv", ["mathos", "-s", "1"])
    main()
    mock_cli_deps["path_num"].assert_called_once_with(1)

def test_cli_flag_latex(monkeypatch, mock_cli_deps):
    # Default (no latex flag) implies deleting tex
    monkeypatch.setattr("sys.argv", ["mathos", "-s", "1"])
    main()
    mock_cli_deps["delete"].assert_called_once_with(Path("dummy.tex"))
    
    mock_cli_deps["delete"].reset_mock()
    
    # With --latex flag, delete should not be called
    monkeypatch.setattr("sys.argv", ["mathos", "-s", "1", "--latex"])
    main()
    mock_cli_deps["delete"].assert_not_called()

def test_cli_flag_open(monkeypatch, mock_cli_deps):
    # Default (no open flag) implies open is not called
    monkeypatch.setattr("sys.argv", ["mathos", "-s", "1"])
    main()
    mock_cli_deps["open"].assert_not_called()
    
    # With --open flag
    monkeypatch.setattr("sys.argv", ["mathos", "-s", "1", "--open"])
    main()
    mock_cli_deps["open"].assert_called_once_with(Path("dummy.pdf"))

def test_cli_flag_file(monkeypatch, mock_cli_deps):
    # Default (no file flag) implies reveal is not called
    monkeypatch.setattr("sys.argv", ["mathos", "-s", "1"])
    main()
    mock_cli_deps["reveal"].assert_not_called()
    
    # With --file flag
    monkeypatch.setattr("sys.argv", ["mathos", "-s", "1", "--file"])
    main()
    mock_cli_deps["reveal"].assert_called_once_with(Path("dummy.pdf"))
    
    mock_cli_deps["reveal"].reset_mock()

    # With -f shorthand
    monkeypatch.setattr("sys.argv", ["mathos", "-s", "1", "-f"])
    main()
    mock_cli_deps["reveal"].assert_called_once_with(Path("dummy.pdf"))

def test_cli_flag_language(monkeypatch, mock_cli_deps):
    # With language
    monkeypatch.setattr("sys.argv", ["mathos", "-s", "1", "--language", "en", "de"])
    main()
    mock_cli_deps["generate"].assert_called_once()
    assert mock_cli_deps["generate"].call_args[0][1] == ["en", "de"]

def test_cli_interactive_selection(monkeypatch, mock_cli_deps):
    monkeypatch.setattr("sys.argv", ["mathos"])
    monkeypatch.setattr("builtins.input", lambda _: "1")
    
    # Patch interactive console prompts
    with patch("apps.cli_client.main.build_printable_setups", return_value=["Option 1"]), \
         patch("apps.cli_client.main.ask_setup", return_value=Path("dummy.json")):
        main()
        
    mock_cli_deps["generate"].assert_called_once()