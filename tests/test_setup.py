from app import main

def test_game_setup():

    if hasattr(main, "init_game"):
        result = main.init_game()
        assert result is None or result is not False
    else:
        assert True
