
from glob import glob



def refactor(string: str) -> str:
    return string.replace("/", ".").replace("\\", ".").replace(".py", "")


pytest_plugins = [
    refactor(fixture) for fixture in glob("fixtures/*.py") if "__" not in fixture
]
