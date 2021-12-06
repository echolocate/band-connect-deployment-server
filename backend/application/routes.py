from application import app, db
from application.models import Band, Agent
from flask import request, jsonify

@app.route('/create/agent', methods=["POST"])
def create_agent():
    json = request.json
    new_agent = Agent(
        name=json["name"],
        phone=json["phone"]
    )
    db.session.add(new_agent)
    db.session.commit()
    return f"Added agent {new_agent.id}: '{new_agent.name}' to database"

@app.route('/read/allAgents', methods=['GET'])
def read_agents():
    all_agents = Agent.query.all()
    json = {"agents": []}
    for agent in all_agents:
        bands = []
        for band in agent.bands:
            bands.append(
                {
                    "id": band.id,
                    "name": band.name,
                    "agent_id": band.agent_id,
                    "phone": band.phone,
                    "audience": band.genre,
                    "members": band.members                   
                }
            )
        json["agents"].append(
            {
                "id": agent.id,
                "name": agent.name,
                "phone": agent.phone,
                "bands": bands
            }
        )
    return jsonify(json)        

@app.route('/update/agent/<int:id>', methods=['PUT'])
def update_agent(id):
    json = request.json
    agent = Agent.query.get(id)
    agent.name = json["name"]
    agent.phone = json["phone"]
    db.session.commit()
    return f"Updated agent (ID: {id}) with name: {agent.name}, phone number {agent.phone}"


@app.route('/create/band/<int:agent_id>', methods=['POST'])
def create_band(agent_id):
    json= request.json
    new_band = Band(
        name=json["name"],
        phone=json["phone"],
        genre = json["genre"],
        members = json["members"],
        agent_id = agent_id
    )
    db.session.add(new_band)
    db.session.commit()
    return f"Added band: '{new_band.name}'"

@app.route('/read/allBands', methods=['GET'])
def read_bands():
    all_bands = Agent.query.all()
    json = {"bands": []}
    for band in all_bands:
        json["bands"].append(
            {
                "id": band.id,
                "name": band.name,
                "phone": band.phone,
                "genre": band.genre,
                "members": band.members
            }
        )
    return jsonify()

@app.route('/update/band/<int:id>', methods=['PUT'])
def update_band(id):
    json = request.json
    bands = Band.query.get(id)
    bands.name = json["name"]
    bands.phone = json["phone"]
    db.session.commit()
    return f"Updated bands (ID: {id}) with name: {bands.name}, phone number {bands.phone}"

@app.route('/delete/band/<int:id>', methods=['DELETE'])
def delete_band(id):
    band = Band.query.get(id)
    db.session.delete(band)
    db.session.commit()
    return f"Band with ID: {id} now deleted"

@app.route('/delete/agent/<int:id>', methods=['DELETE'])
def delete_agent(id):
    agent = Agent.query.get(id)
    db.session.delete(agent)
    db.session.commit()
    return f"Agent with ID: {id} now deleted"