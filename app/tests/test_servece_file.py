import pytest

from app.services import files
from . import filename


@pytest.mark.asyncio
async def test_write_read_file():
    data = {'test': 'data'}
    await files.write_to_file(filename, data)
    read_data = await files.read_from_file(filename)
    assert data == read_data


@pytest.mark.asyncio
async def test_add_to_file():
    data = {'test': 'data'}
    appended_data = {'test2': [1, 2, 3, '4']}

    await files.write_to_file(filename, data)
    await files.add_in_file(filename, appended_data)
    read_data = await files.read_from_file(filename)
    assert data['test'] == read_data['test']
    assert appended_data['test2'] == read_data['test2']
