from subscriptions.datastore import db, add_schema


@add_schema
class SampleModel(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    started_at = db.Column(db.DateTime)
    ended_at = db.Column(db.DateTime)
    description = db.Column(db.Text())
