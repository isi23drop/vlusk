from app.models.machine import Lecture
from app.services.lecture import (
        get_all_lectures, get_lecture,
        update_lecture, delete_lecture
        )


def get_all_lec_ctr():
    return get_all_lectures(Lecture)


def get_lec_ctr(id):
    return get_lecture(Lecture, id)


def update_lec_ctr(id):
    return update_lecture(Lecture, id)


def delete_lec_ctr(id):
    return delete_lecture(Lecture, id)
