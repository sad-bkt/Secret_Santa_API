from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blueprints.page import blueprint as page
from blueprints.swagger import blueprint as final_servis


app = Flask(__name__)
app.register_blueprint(page)
app.register_blueprint(final_servis)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False) # , unique=True
    description = db.Column(db.String)
    participants = db.relationship('participants', backref='Participants', lazy=True)


class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    wish = db.Column(db.String)
    recipient = db.Column(db.Participant)
    a = db.relationship()


# group_participant = db.Table(
#     "group_participant",
#     sa.Column("user_id", sa.ForeignKey(User.id), primary_key=True),
#     sa.Column("book_id", sa.ForeignKey(Book.id), primary_key=True),
# ) (db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     group = db.Column(db.String)
#     recipient = db.Column(db.String)

with app.app_context():
    db.create_all()

    # db.session.add(Participant(username="example"))
    # db.session.commit()
    #
    # users = db.session.execute(db.select(User)).scalars()


# @app.route("/group", methods=['POST'])
# # @api.doc(params={'id': 'An ID'})
# def add_group():
#     request.
#     return {
#         'name': 'string',
#         'description': 'string',
#     }


if __name__ == '__main__':
    app.run(debug=True, port=8080)
