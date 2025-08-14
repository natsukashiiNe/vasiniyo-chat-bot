from decimal import Decimal
import itertools
import logging
import time

logger = logging.getLogger(__name__)
_next_id = itertools.count(1001)


def new_quiz_id():
    return next(_next_id)


def now():
    return time.monotonic()


def _parse_player_count(players, count):
    """
    Returns INTEGER number of playes from either (int | X%) input
    """
    player_count = len(players)
    if isinstance(count, int):
        return max(0, min(count, player_count))

    if isinstance(count, str):
        percent_text = count.strip()
        percent_value = Decimal(percent_text[:-1].strip())

        if percent_value <= 0 or player_count == 0:
            return 0

        ratio = percent_value / 100
        raw_selection = Decimal(player_count) * ratio
        selected_count = int(raw_selection)
        return min(selected_count, player_count)
    return player_count


def build_change_inventory_action(player_count, item_name, delta):
    def apply_change(sorted_users):
        count = _parse_player_count(len(sorted_users), player_count)
        if delta > 0:
            affected = sorted_users[:count]
        else:
            affected = sorted_users[-count:]

        for user in affected:
            # NOTE: remove this? this should never happen?
            if item_name not in user["inventory"]:
                user["inventory"][item_name] = 0
            user["inventory"][item_name] += delta

        logger.info(
            "Applied inventory change of %s %s to %s users",
            delta,
            item_name,
            len(affected),
        )

    return apply_change
