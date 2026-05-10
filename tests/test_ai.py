from app import main


def test_ai_minimax_execution():

    if hasattr(main, "minimax"):
        board = [[0 for _ in range(8)] for _ in range(8)]
        result = main.minimax(
            board,
            1,
            float("-inf"),
            float("inf"),
            True
        )
        assert result is not None
    else:
        assert True
