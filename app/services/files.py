import json
import aiofiles

__all__ = ['read_from_file', 'write_to_file', 'add_in_file']


async def read_from_file(filename):
    async with aiofiles.open(filename, 'r') as f:
        data = json.loads(await f.read())
        await f.close()
        return data


async def write_to_file(filename, data):
    async with aiofiles.open(filename, 'w') as f:
        await f.write(json.dumps(data))
        await f.close()


async def add_in_file(filename, data):
    old_data = await read_from_file(filename)
    old_data.update(data)
    await write_to_file(filename, old_data)

