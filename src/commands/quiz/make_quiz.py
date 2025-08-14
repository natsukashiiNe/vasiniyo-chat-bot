import logging

from quiz.cli.requests import (
    get_challenged_id,
    get_question_settings,
    get_sender_id,
    setup_duel_settings,
)

logger = logging.getLogger(__name__)

QUIZZES = {
    # quiz_id: {
    #   'users': [{id, state: ready | not ready, score} ... ]
    #   'questions': [{text, options, correct_answer}],
    #   'current_question': int,
    #   'question_settings': {
    #       'time_to_answer': int
    #       'themes' : [...]
    #       'diff' : [min, max]
    #    }
    #    'quiz_settings': {
    #       'stop_condition': required_score | question_count
    #       'rewards' : some_funcs(top_player_count, actions)
    #       'penalty' : some_funcs(worst_plyaer_count, actions)
    #    }
}


# ---- STOP STRATS ------------------------------------------------------------
def _stop_by_question_count(quiz, max_questions):
    return quiz["current_question"] >= max_questions


def _stop_by_required_score(quiz, required_score):
    return any(
        user["score"] >= required_score for user in quiz["users"].values()
    )


STOP_STRATEGIES = {
    "question_count": _stop_by_question_count,
    "score_count": _stop_by_required_score,
}
# ---- STOP STRATS -------------------------------------------------------------


# ---- QUIZ USAGE -------------------------------------------------------------
def try_make_quiz(qtype):
    if qtype == "duel":
        return _request_duel(
            get_sender_id(),
            get_challenged_id(),
            get_question_settings(),
            setup_duel_settings(),
        )
    # TODO if qtype == "ffa":
    # TODO if qtype == "daily":


def end_quiz(quiz_id):
    quiz = QUIZZES[quiz_id]
    sorted_users = sorted(quiz["users"], key=lambda u: u["score"], reverse=True)

    reward_action = quiz["quiz_settings"].get("rewards")
    penalty_action = quiz["quiz_settings"].get("penalty")

    if callable(reward_action):
        reward_action(sorted_users)

    if callable(penalty_action):
        penalty_action(sorted_users)

    # TODO Mark quiz as ended, or remove from QUIZZES. Or do some states idk
    logger.info("[QUIZ] %s has ended.", quiz_id)
    logger.info(
        "Scores were: %s", [(u["id"], u["score"]) for u in sorted_users]
    )


# ------------------------------------------------------------------------------


# ---- TRY MAKING QUIZES -------------------------------------------------------
def _request_duel(id1, id2, question_settings, quiz_settings):
    accepted = True
    # send(id2, f"[DUEL] {id1} challenges you.")
    # offered = stake or {"item": "coins", "amount": 0}
    # send(id2, f"[DUEL] stake is {offered}")
    # resp = ask(id2, "your choice", timeout=10.0)
    # accept / deny / offer new stake

    # if accepted:
    # QUIZZES[qid]"
    #   'users' = [{id = id1, state = not ready, score = 0} ... ]
    #   'questions' = get_default_question(),
    #   'current_question' = 0,
    #   'question_settings' = question_settings
    #   'quiz_settings': quiz_settings
    #    }
    return accepted


# ------------------------------------------------------------------------------
