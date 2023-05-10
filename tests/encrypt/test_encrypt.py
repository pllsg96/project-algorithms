from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("a", "b")

    with pytest.raises(TypeError):
        encrypt_message(1, 2)

    assert encrypt_message("pizza", 0) == "azzip"
    assert encrypt_message("champignon", 3) == "ahc_nongipm"
    assert encrypt_message("calabresa", 4) == "aserb_alac"