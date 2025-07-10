from src.object_commands import type_check
import pytest


@type_check
def dummy(filename, data):
    return True


def test_valid_type():
    assert dummy("file.json", {}) == True


def test_invalid_filename():
    with pytest.raises(TypeError):
        dummy(["file"], {})


def test_invalid_data():
    with pytest.raises(TypeError):
        dummy("file.json", "not a dict")