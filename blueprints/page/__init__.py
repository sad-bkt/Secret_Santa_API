from flask import Blueprint, request, jsonify

from main import Participant, Group, db

blueprint = Blueprint('', __name__)


@blueprint.route('/group', methods=['POST'])
def add_group():
    #TODO if request.form["name"] == '':

    group = Group(
        name=request.form["name"],
        description=request.form["description"],
    )
    db.session.add(group)
    db.session.commit()
    return group.id


@blueprint.route('/groups', methods=['GET'])
def get_groups():
    groups = db.get_or_404(Group)
    # return json.dumps({ #TODO без указания участников
    #     "id": groups.id,
    #     "name": groups.name,
    #     "description": groups.description,
    # }), 200
        # {c.name: getattr(groups, c.name) for c in groups.__table__.columns}
    #jsonify(db.get_or_404(Group)), 200


@blueprint.route('/group/<int:id>', methods=['GET'])
def get_group(id):
    return jsonify(db.get_or_404(Group, id)), 200


@blueprint.route('/group/<int:id>', methods=['PUT'])
def put_group(id):
    group = db.get_or_404(Group, id)
    if 'name' != '':
        group.name = request.form["name"]
        group.description = request.form["description"]
        db.session.commit()
    else:
        return '', 400
        #TODO error


@blueprint.route('/group/<int:id>', methods=['DELETE'])
def delete_group(id):
    group = db.get_or_404(Group, id)
    db.session.delete(group)
    db.session.commit()


@blueprint.route('/group/<int:id>/participant/', methods=['POST'])
def add_participant_in_group(id):
    group = db.get_or_404(Group, id)
    participant = Participant(
        name=request.form["name"],
        wish=request.form["wish"],)
    db.session.add(participant)
    group.participants.add(participant)
    db.session.commit()
    return participant.id, 200


@blueprint.route('/group/<int:id_g>/participant/<int:id_p>', methods=['DELETE'])
def delete_participant_from_group(id_g, id_p):
    group = db.get_or_404(Group, id_g)
    participant = db.get_or_404(group.participants, id_p)
    db.session.delete(participant)
    db.session.commit()


@blueprint.route('/group/<int:id>/toss', methods=['POST'])
def toss(id):
    return db.get_or_404(Group)


@blueprint.route('/group/<int:id_g>/participant/<int:id_p>/recipient', methods=['GET'])
def post_participant_in_group(id_g, id_p):
    return db.get_or_404(Group)
