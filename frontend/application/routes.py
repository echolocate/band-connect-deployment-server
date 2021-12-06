from application import app
from application.forms import CreateBandForm, CreateAgentForm
from flask import render_template, request, redirect, url_for
import requests

@app.route('/', methods=["GET"])
def home():
    agents = requests.get(f"http://bc-backend:5000/read/allAgents").json()["agents"]
    return render_template("index.html", title="Home", agents=agents)

@app.route('/create/agent', methods=["GET", "POST"])
def create_agent():
    form = CreateAgentForm()

    if request.method == "POST":
        response = requests.post(
            f"http://bc-backend:5000/create/agent",
            json={
                "name": form.name.data,
                "phone": form.phone.data                
            }
        )
        return redirect(url_for("home"))

    return render_template("create_agent.html", title="Add Agent", form=form)

@app.route('/create/band', methods=['GET', 'POST'])
def create_band():
    form = CreateBandForm()

    json = requests.get(f"http://bc-backend:5000/read/allAgents").json()
    for agent in json["agents"]:
        form.agent.choices.append((agent["id"], agent["name"]))

    if request.method == "POST":
        response = requests.post(
            f"http://bc-backend:5000/create/band/{form.agent.data}",
            json={
                "name": form.name.data,
                "phone": form.phone.data,
                "genre": form.genre.data,
                "members": form.members.data
            }
        )
        return redirect(url_for("home"))

    return render_template("create_band.html", title="Add Band", form=form)

@app.route('/read/allAgents', methods=['GET'])
def read_agents():
    
    agents = requests.get(f"http://{backend}/read/allAgents").json()["agents"]
    return render_template("read_agents.html", title="Agents", agents=agents)

@app.route('/read/allBands', methods=['GET'])
def read_bands():
    form = ViewBandsForm()

    bands = requests.get(f"http://{backend}/read/allBands").json()["bands"]
    return render_template("read_bands.html", title="Bands", bands=bands)

