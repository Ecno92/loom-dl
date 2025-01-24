import pytest
from loomdl import extract_id


@pytest.mark.parametrize(
    "url",
    [
        "https://www.loom.com/share/37291eb61a694839a75c71c6ef24404c",
        "https://www.loom.com/share/37291eb61a694839a75c71c6ef24404c?sid=f4931847-da55-11ef-9c93-0050b68f58ff&bla=xx",
    ],
)
def test_extract_id(url):
    assert extract_id(url) == "37291eb61a694839a75c71c6ef24404c"
