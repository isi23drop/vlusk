from app.models.machine import Alumni
from app.services.alumni import (
        get_all_alumni, get_alumni,
        update_alumni, delete_alumni
        )


def get_all_alumni_ctr():
    return get_all_alumni(Alumni)


def get_alumni_ctr(id):
    return get_alumni(Alumni, id)


def update_alumni_ctr():
    return update_alumni(Alumni)


def delete_alumni_ctr():
    return delete_alumni(Alumni)
