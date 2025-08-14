import pytest

from src.commands.quiz.utils import _parse_player_count

CASES = [
    ([0] * 10, 5, 5),
    ([0] * 10, 20, 10),
    # --
    ([0] * 10, "50%", 5),
    ([0] * 10, "52%", 5),
    ([0] * 10, "59%", 5),
    ([0] * 10, "150%", 10),
    ([0] * 10, "1%", 0),
]


def case_id(c):
    players, count, expected = c
    return f"n={len(players)}, {count}->{expected}"


@pytest.mark.parametrize(
    "players,count,expected", CASES, ids=[case_id(c) for c in CASES]
)
def test_parse_player_count(players, count, expected):
    assert _parse_player_count(players, count) == expected
