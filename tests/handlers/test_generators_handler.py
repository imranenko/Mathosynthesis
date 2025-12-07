# test_generators_handler.py

import json
import builtins
from pathlib import Path
import pytest

from mathosynthesis.handlers.generators_handler import (
    read_json,
    generate_setup,
    _generate_block,
)


# ---------------------------
# read_json
# ---------------------------

def test_read_json_success(monkeypatch):
    fake_data = {"a": 1}

    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO(json.dumps(fake_data))

    monkeypatch.setattr(builtins, "open", mock_open)

    result = read_json("dummy.json")
    assert result == fake_data


def test_read_json_file_not_found(monkeypatch):
    def mock_open(*args, **kwargs):
        raise FileNotFoundError

    monkeypatch.setattr(builtins, "open", mock_open)

    with pytest.raises(FileNotFoundError):
        read_json("missing.json")


def test_read_json_invalid_json(monkeypatch):
    def mock_open(*args, **kwargs):
        from io import StringIO
        return StringIO("{invalid json}")

    monkeypatch.setattr(builtins, "open", mock_open)

    with pytest.raises(ValueError):
        read_json("invalid.json")


# ---------------------------
# generate_setup
# ---------------------------

def test_generate_setup_success(monkeypatch):
    # Mock register
    fake_tasks = ["x+1", "2y"]
    register_mock = {"task1": lambda settings: fake_tasks}
    monkeypatch.setattr(
        "mathosynthesis.handlers.generators_handler.register",
        register_mock
    )

    json_data = {
        "task_blocks": [
            {
                "id": "task1",
                "settings": {"dummy": 1},
                "columns": 2,
                "description": {
                    "en": "Example English block",
                    "de": "Beispiel Deutsch"
                },
            }
        ]
    }

    result = generate_setup(json_data, preferred_languages=["de", "en"])
    assert any("Beispiel Deutsch" in line for line in result)
    assert any("\\begin{multicols}{2}" in line for line in result)
    assert any("\\item $x+1$" in line for line in result)


def test_generate_setup_missing_keys(monkeypatch):
    json_data = {"task_blocks": [{"id": "x"}]}  # missing settings + columns

    with pytest.raises(ValueError):
        generate_setup(json_data)


def test_generate_setup_language_fallback(monkeypatch):
    fake_tasks = ["7+3"]
    register_mock = {"id1": lambda s: fake_tasks}
    monkeypatch.setattr(
        "mathosynthesis.handlers.generators_handler.register",
        register_mock
    )

    data = {
        "task_blocks": [
            {
                "id": "id1",
                "settings": {},
                "columns": 1,
                "description": {"en": "English desc"}
            }
        ]
    }

    result = generate_setup(data, ["fr", "en"])
    assert "English desc" in result


# ---------------------------
# _generate_block
# ---------------------------

def test_generate_block_multi_column():
    tasks = ["a", "b"]
    result = _generate_block(tasks, columns=2)

    assert "\\begin{multicols}{2}" in result
    assert "\\item $a$" in result
    assert "\\end{multicols}" in result


def test_generate_block_single_column():
    tasks = ["x"]
    result = _generate_block(tasks, columns=1)

    assert "\\begin{enumerate}" in result
    assert "\\item $x$" in result
    assert "\\end{enumerate}" in result