from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Agent, Band

test_band={
    "id": 1,
    "name": "The Rutles",
    "phone": "123456789"
    }
        
test_agent={
    "id": 1,
    "agent_name": "Leggy Mountbatten",
    "phone": "987654321"
    }

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()
        db.session.add(Band(name="La Garcon De La Plage"))
        db.session.add(Band(phone="34567654321"))
        db.session.add(Agent(name="Ron DeKlein"))
        db.session.add(Agent(phone="9999999999"))
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()

class TestRead(TestBase):

    def test_read_all_agents(self):
        response = self.client.get(url_for('read_agents'))
        all_agents = { "agents": [test_agent] }
        self.assertEquals(all_agents, response.json)
    
    def test_read_agent(self):
        response = self.client.get(url_for('read_agent'))
        self.assertEquals(test_agent, response.json)

    def test_read_all_bands(self):
        response = self.client.get(url_for('read_bands'))
        all_bands = { "bands": [test_band] }
        self.assertEquals(all_bands, response.json)
    
    def test_read_band(self):
        response = self.client.get(url_for('read_band', id=1))
        self.assertEquals(test_band, response.json)

class TestCreate(TestBase):

    def test_create_agent(self):
        response = self.client.post(
            url_for('create_agent'),
            json={"agent_name": "Dick Jaws", "phone":"0123456789"},
            follow_redirects=True
        )
        self.assertEquals(b"Added agent: Dick Jaws", response.data)
        self.assertEquals(Agent.query.get(2).agent_name, "Dick Jaws")
    
class TestUpdate(TestBase):

    def test_update_agent(self):
        response = self.client.put(
            url_for('update_agent', id=1),
            json={"name": "Dick Jaws"}
        )
        self.assertEquals(b"Updated agent (ID: 1) with name: Dick Jaws", response.data)
        self.assertEquals(Agent.query.get(1).name, "Dick Jaws")

    def test_update_band(self):
        response = self.client.put(
            url_for('update_band', id=1),
            json={"name": "Conner4Real","phone":"444444444444"}
        )
        self.assertEquals(b"Updated Band (ID: 1) with name: Conner4Real, phone number 444444444444", response.data)
        self.assertEquals(Band.query.get(1).name, "Conner4Real")
        self.assertEquals(Band.query.get(1).phone, "444444444444")
    
class TestDelete(TestBase):

    def test_delete_band(self):
        response = self.client.delete(url_for('delete_band', id=1)),
        self.assertEquals(b"Band with ID: 1 now deleted", response.data)
        self.assertIsNone(Band.query.get(1))