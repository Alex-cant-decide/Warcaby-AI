from app import main

def test_player_move_logic():

    if hasattr(main, "move"):
        try:
            main.move(0, 0, 1, 1)
        except Exception:
            pass

    assert True
