from kata.array.problems.rank import rank, track


class TestRank:
    def test(self) -> None:
        root = track(5)
        assert rank(5, root) == 0
        root = track(1, root)
        assert rank(5, root) == 1
        assert rank(1, root) == 0
        root = track(4, root)
        assert rank(5, root) == 2
        assert rank(1, root) == 0
        assert rank(4, root) == 1
        root = track(4, root)
        assert rank(5, root) == 3
        assert rank(1, root) == 0
        assert rank(4, root) == 2
        root = track(5, root)
        assert rank(5, root) == 4
        assert rank(1, root) == 0
        assert rank(4, root) == 2
        root = track(9, root)
        assert rank(5, root) == 4
        assert rank(1, root) == 0
        assert rank(4, root) == 2
        assert rank(9, root) == 5
        root = track(7, root)
        assert rank(5, root) == 4
        assert rank(1, root) == 0
        assert rank(4, root) == 2
        assert rank(9, root) == 6
        assert rank(7, root) == 5
        root = track(13, root)
        assert rank(5, root) == 4
        assert rank(1, root) == 0
        assert rank(4, root) == 2
        assert rank(9, root) == 6
        assert rank(7, root) == 5
        assert rank(13, root) == 7
        root = track(3, root)
        assert rank(5, root) == 5
        assert rank(1, root) == 0
        assert rank(4, root) == 3
        assert rank(9, root) == 7
        assert rank(7, root) == 6
        assert rank(13, root) == 8
        assert rank(3, root) == 1
        assert rank(0, root) == -1
        assert rank(2, root) == -1
        assert rank(6, root) == -1
        assert rank(8, root) == -1
