from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CreateAgentForm(FlaskForm):
    name = StringField("Agent Name", validators=[DataRequired()])
    phone = StringField("Phone", validators=[DataRequired()])
    submit = SubmitField("Add Agent")

class CreateBandForm(FlaskForm):
    name = StringField("Band Name", validators=[DataRequired()])
    phone = StringField("Phone", validators=[DataRequired()])
    genre = SelectField("Audience", validators=[DataRequired()],
        choices=[
            ('Children', 'Children'),
            ('Teenager', 'Teenager'),
            ('Adult', 'Adult'),
            ('Hardcore', 'Hardcore')
        ]
    )
    members = StringField("Members", validators=[DataRequired()])
    agent = SelectField("Agent", validators=[DataRequired()], choices=[])    
    submit = SubmitField("Add Band")

# class ViewAgentsForm(FlaskForm):
#     agent = SelectField('Agent', validators=[DataRequired()], choices=[])
#     submit = SubmitField("View Agent")