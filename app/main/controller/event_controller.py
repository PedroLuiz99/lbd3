from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required
from ..util.dto import EventDto
from ..service.event_service import save_new_event, get_all_events, get_a_event

api = EventDto.api
_event = EventDto.event


@api.route('/')
class EventList(Resource):
    @api.doc('list_of_registered_events')
    @api.marshal_list_with(_event, envelope='data')
    @api.doc(security="Login_Token")
    @token_required
    def get(self):
        """List all registered events"""
        return get_all_events()

    @api.expect(_event, validate=True)
    @api.response(201, 'Event successfully created.')
    @api.doc('create a new event')
    @api.doc(security="Login_Token")
    def post(self):
        """Creates a new Event """
        data = request.json
        return save_new_event(data=data)


@api.route('/<event_id>')
@api.param('event_id', 'The Event identifier')
@api.response(404, 'Event not found.')
class Event(Resource):
    @api.doc('get a event')
    @api.marshal_with(_event)
    @api.doc(security="Login_Token")
    def get(self, event_id):
        """get a event given its identifier"""
        event = get_a_event(event_id)
        if not event:
            api.abort(404)
        else:
            return event
