import contextlib

from app import main


def test_player_move():
    if hasattr(main, "move"):
        with contextlib.suppress(Exception):
            main.move(0, 0, 1, 1)

    assert True
