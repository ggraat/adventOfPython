from pathlib import Path


def read_lines(filename: str) -> []:
    content = get_resource_path(filename).read_text(encoding='utf-8')
    return content.splitlines()


def read_line(filename: str) -> str:
    with get_resource_path(filename).open(mode='r', encoding='utf-8') as file:
        yield from file


def get_resource_path(filename):
    return Path('resources') / Path(filename)
