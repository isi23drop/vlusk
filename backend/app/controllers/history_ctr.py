from app.models.machine import History
from app.services.history import (
        get_all_hist, get_term,
        update_history, delete_history, get_by_lecture
        )


def get_all_hist_ctr():
    return get_all_hist(History)


def get_by_lecture_ctr(id_lecture, id_alumni):
    return get_by_lecture(History, id_lecture=id_lecture, id_alumni=id_alumni)


def get_hist_term_ctr(id_alumni, id_lecture):
    return get_term(History, id_alumni=id_alumni, id_lecture=id_lecture)


def update_ctr(id_alumni, id_lecture):
    return update_history(History, id_alumni=id_alumni, id_lecture=id_lecture)


def delete_ctr(id_alumni, id_lecture):
    return delete_history(History, id_alumni=id_alumni, id_lecture=id_lecture)
