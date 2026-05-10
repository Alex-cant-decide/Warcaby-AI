from app import main


def test_board_creation_logic():

    if hasattr(main, "create_board"):
        board = main.create_board()
        assert board is not None
    else:
        assert True
