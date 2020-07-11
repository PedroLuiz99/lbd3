from .. import db
from sqlalchemy import or_, and_


class Event(db.Model):
    """ Event Model for storing event related details """
    __tablename__ = "event"

    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    event_name = db.Column(db.String(50))
    event_description = db.Column(db.String(255))
    date_start = db.Column(db.DateTime, nullable=False)
    date_end = db.Column(db.DateTime, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def check_conflicting_event(self):
        has_event = Event.query. \
            filter(Event.user_id == self.user_id). \
            filter(Event.event_id != self.event_id). \
            filter(Event.active). \
            filter(
            or_(
                (and_(Event.date_start < self.date_start, Event.date_end >= self.date_start)),
                (and_(Event.date_start >= self.date_start, Event.date_end <= self.date_end)),
                (and_(Event.date_start > self.date_start, Event.date_end < self.date_end)),
                (and_(Event.date_start <= self.date_end, Event.date_end > self.date_end))
            )
        ).first()
        return has_event

    def __repr__(self):
        return "<Event '{}'>".format(self.username)
