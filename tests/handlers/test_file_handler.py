import os
import subprocess
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock, call

from mathosynthesis.handlers import files_handler

@pytest.fixture
def temp_folder(tmp_path):
    return tmp_path / "test_folder"

def test_get_timestamp_format():
    ts = files_handler._get_timestamp(week_date_format=True)
    assert "W" in ts  # ISO week format contains 'W'
    ts2 = files_handler._get_timestamp(week_date_format=False)
    assert "-" in ts2 and "T" in ts2  # Standard format

def test_create_folder_creates_and_handles_error(tmp_path):
    folder = tmp_path / "new_folder"
    files_handler.create_folder(folder)
    assert folder.exists()
    # Simulate OSError by patching os.makedirs to raise
    with patch("os.makedirs", side_effect=OSError("fail")) as mock_makedirs:
        files_handler.create_folder(folder)
        mock_makedirs.assert_called_once()

def test_create_md_writes_lines(tmp_path):
    file_path = tmp_path / "test.md"
    content = ["line1", "line2", "line3"]
    files_handler.create_md(content, file_path)
    with open(file_path) as f:
        lines = f.read().splitlines()
    assert lines == content

@patch("subprocess.run")
def test_create_pdf_runs_pandoc_success(mock_run, tmp_path):
    md_path = tmp_path / "input.md"
    pdf_path = tmp_path / "output.pdf"
    # Create dummy md file
    md_path.write_text("# Test")
    files_handler.create_pdf(md_path, pdf_path)
    mock_run.assert_called_once()
    cmd = mock_run.call_args[0][0]
    cmd_strs = list(map(str, cmd))
    assert "pandoc" in cmd_strs[0]
    assert str(md_path) in cmd_strs
    assert str(pdf_path) in cmd_strs

@patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "cmd"))
def test_create_pdf_logs_error_on_failure(mock_run):
    with patch("logging.Logger.error") as mock_log_error:
        files_handler.create_pdf("input.md", "output.pdf")
        mock_log_error.assert_called_with("Pandoc conversion failed!")

@patch("subprocess.run")
def test_open_file_calls_open_command(mock_run):
    files_handler.open_file("somefile.pdf")
    mock_run.assert_called_once_with(["open", "somefile.pdf"], check=True)

@patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "cmd"))
def test_open_file_logs_error_on_failure(mock_run):
    with patch("logging.Logger.error") as mock_log_error:
        files_handler.open_file("somefile.pdf")
        mock_log_error.assert_called()

def test_delete_file_success(tmp_path):
    file_path = tmp_path / "delete_me.txt"
    file_path.write_text("delete")
    files_handler.delete_file(file_path)
    assert not file_path.exists()

def test_delete_file_not_found_logs_error(tmp_path):
    fake_path = tmp_path / "nonexistent.txt"
    with patch("logging.Logger.error") as mock_log_error:
        files_handler.delete_file(fake_path)
        mock_log_error.assert_called_with("File not found!")

def test_delete_file_os_error(tmp_path):
    file_path = tmp_path / "file.txt"
    file_path.write_text("data")
    with patch("os.remove", side_effect=OSError("fail")):
        with patch("logging.Logger.error") as mock_log_error:
            files_handler.delete_file(file_path)
            mock_log_error.assert_called()

@patch("subprocess.run")
def test_reveal_file_calls_open_r(mock_run):
    files_handler.reveal_file("file.pdf")
    mock_run.assert_called_once_with(["open", "-R", "file.pdf"], check=True)

@patch("subprocess.run", side_effect=OSError("fail"))
def test_reveal_file_logs_error_on_failure(mock_run):
    with patch("logging.Logger.error") as mock_log_error:
        files_handler.reveal_file("file.pdf")
        mock_log_error.assert_called()

def test_get_base_path_returns_path_with_timestamp(monkeypatch):
    monkeypatch.setattr(files_handler, "_get_timestamp", lambda: "2025-12-05T10-20-30")
    base_path = files_handler.get_base_path("testfile")
    assert "testfile_2025-12-05T10-20-30" in str(base_path)

def test_get_setups_returns_dict(tmp_path):
    setups_dir = tmp_path
    # Create files and folders
    (setups_dir / "setup1.json").write_text("{}")
    category = setups_dir / "category1"
    category.mkdir()
    (category / "setup2.json").write_text("{}")

    # Patch SETUPS_DIR to tmp_path
    with patch("mathosynthesis.handlers.files_handler.SETUPS_DIR", str(setups_dir)):
        setups = files_handler.get_setups()

    assert "NO_CATEGORY" in setups
    assert "category1" in setups
    assert setups["NO_CATEGORY"] == ["setup1.json"]
    assert setups["category1"] == ["setup2.json"]

def test_get_setups_logs_error_and_returns_none(tmp_path):
    with patch("mathosynthesis.handlers.files_handler.SETUPS_DIR", str(tmp_path)):
        with patch("logging.Logger.error") as mock_log_error:
            result = files_handler.get_setups()
            assert result is None
            mock_log_error.assert_called_with("No setups found!")