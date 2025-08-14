import logging

from quiz.utils import build_change_inventory_action

logger = logging.getLogger(__name__)

# ---- DEFAULT TEST CONFIG -----------------------------------------------------
PLAYERS = (
    {"id": 1000, "inventory": {"coins": 1000, "honor": 100}},
    {"id": 2000, "inventory": {"coins": 2000, "honor": 200}},
    {"id": 3000, "inventory": {"coins": 3000, "honor": 300}},
    {"id": 4000, "inventory": {"coins": 4000, "honor": 400}},
    {"id": 5000, "inventory": {"coins": 5000, "honor": 500}},
)

default_questions = (
    {"text": "Choose 1", "options": ["1", "2", "3", "4"], "answer": "1"},
    {"text": "Choose 2", "options": ["1", "2", "3", "4"], "answer": "2"},
    {"text": "Choose 3", "options": ["1", "2", "3", "4"], "answer": "3"},
    {"text": "Choose 4", "options": ["1", "2", "3", "4"], "answer": "4"},
    {"text": "Choose 5", "options": ["1", "2", "3", "4"], "answer": "5"},
)

default_stake = {"item": "honor", "amount": "20"}
default_question_settings = {"qtimer": 30, "themes": "all", "diff": "all"}
default_duel_settings = {
    "stop_condition": {"key": "score_count", "values": {"3"}},
    "rewards": "",
    "penalty": "",
}
# ------------------------------------------------------------------------------


# ---- TG API DATA -------------------------------------------------------------
def get_sender_id():
    return PLAYERS[0]["id"]


def get_challenged_id():
    return PLAYERS[1]["id"]


# ------------------------------------------------------------------------------


# ---- TG INPUT DATA -----------------------------------------------------------
def setup_duel_settings():
    return {
        "stop_condition": {"key": "score_count", "values": 3},
        "rewards": build_change_inventory_action(
            player_count=1,
            item_name=default_stake["item"],
            delta=default_stake["amount"],
        ),
        "penalty": build_change_inventory_action(
            player_count=1,
            item_name=default_stake["item"],
            delta=-1 * default_stake["amount"],
        ),
    }


def get_question_settings():
    return default_question_settings


# ------------------------------------------------------------------------------
