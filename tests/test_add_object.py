import pytest 
from src.handle_data import add_object


def test_add_object_success():

    data = {'kitchen': {'objects': {}}}

    result = add_object(data, ['kitchen'], 'chair', 'furniture')
    assert result['kitchen']['objects']['chair'] == {'category': 'furniture'}


def test_add_object_success_in_nested_dict():

    data = {'level1': {'level2': {'objects': {}}}}

    result = add_object(data, ['level1', 'level2'], 'object_added', 'success')
    assert result['level1']['level2']['objects']['object_added'] == {'category': 'success'}


def test_invalid_path_returns_false():

    data = {'kitchen': {'objects': {}}}

    result = add_object(data, ['bedroom'], 'apple', 'fruit')
    assert result is False


def test_missing_objects_key_returns_false():

    data = {'room': {}}

    result = add_object(data, ['room'], 'chair', 'furniture')
    assert result is False


def test_add_object_root_level():

    data = {'objects': {}}
    
    result = add_object(data, [], 'key', 'tool')
    assert result['objects']['key'] == {'category': 'tool'}


def test_invalid_data_type_raises():

    with pytest.raises(TypeError):
        add_object("not a dict", ['room'], 'chair', 'furniture')


def test_invalid_path_type_raises():

    with pytest.raises(TypeError):
        add_object({}, 'room', 'chair', 'furniture')


def test_invalid_name_type_raises():

    with pytest.raises(TypeError):
        add_object({}, [], 123, 'furniture')


def test_invalid_category_type_raises():

    with pytest.raises(TypeError):
        add_object({}, [], 'chair', 123)