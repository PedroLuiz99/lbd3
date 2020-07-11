import uuid
import datetime

from app.main import db
from app.main.model.event import Event


def save_new_event(data):
    new_event = Event(
        user_id=data['user_id'],
        event_name=data['event_name'],
        event_description=data['event_description'],
        date_start=data['date_start'],
        date_end=data['date_end'],
        active=data['active'],
    )

    c_event = new_event.check_conflicting_event()
    if c_event:
        return {"message": "Event date conflicts with event {}".format(c_event.event_name)}, 409

    save_changes(new_event)
    # TODO: AJUSTAR RETORNO
    return None, 201


def put_event(event_id, data):
    event = Event.query.filter_by(event_id=event_id).first()
    if event:
        event.event_name = data['event_name']
        event.event_description = data['event_description']
        event.date_start = data['date_start']
        event.date_end = data['date_end']
        event.active = data['active']

        c_event = event.check_conflicting_event()
        if c_event:
            return {"message": "Event date conflicts with event {}".format(c_event.event_name)}, 409

        db.session.commi()
        return event
    else:
        response_object = {
            'message': 'Event not found',
        }
        return response_object, 404


def get_all_events():
    # TODO: FILTRAR POR USUARIO
    return Event.query.all()


def get_a_event(event_id):
    return Event.query.filter_by(event_id=event_id).first()


def delete_event(event_id):
    event = get_a_event(event_id)
    try:
        if event:
            db.session.delete(event)
            return None, 204
    except Exception as e:
        return {"message": "Error deleting the event"}, 409


def patch_event(event_id, data):
    event = get_a_event(event_id)
    try:
        if event:
            for field in data:
                setattr(event, field, data[field])

            c_event = event.check_conflicting_event()
            if c_event:
                return {"message": "Event date conflicts with event {}".format(c_event.event_name)}, 409

    except Exception as e:
        return {"message": "Error deleting the event"}, 409


def save_changes(data):
    db.session.add(data)
    db.session.commit()
