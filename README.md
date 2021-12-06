# Band Connect Web App

## Brief
As a final individual project on the QA DevOps Boot Camp we were asked to write a web application to achieve the following objectives:
"
* To create a multi-tier web application that demonstrates CRUD functionality.
* To utilise containers to host and deploy the application.
* To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application.
"

This will showcase all the topics we have learned over a nine week period.

### Additional Requirements
The components required to demonstrate the objective were as follows:

* A Project board in GitHub
* A MySQL Database for Azure, consisting of at least two tables that model a relationship
* A Flask driven frontend service to host the web pages that will implement CRUD capability to retrieve information from this database
* Automated unit testing using pytest in a CI/CD pipeline, implemented using Jenkins inside a Docker container
* Use of git and GitHub within Jenkins to orchestrate development to the Azure virtual machine

### Implementation
To achieve the requirements I initially set out to produce a website which would allow fledgling musicians to book gigs online with venues (pubs and clubs primarily).
After a reviewing this specification I came to the conclusion that this would require a many-to-many relationship and may be a bit ambitious for a first project, especially given the time constraint.
Eventually I settled on an agent to band relationship as this would pare it down to a the 'one agent has many bands, a band has only one agent' scenario, modelling a simpler one to many relationship.

Original idea with extra table for band members.
https://1drv.ms/u/s!Aq2hJel0GwxWpCduPu0Yk4yZCQcE?e=zfe2iE

Eventually simplified to:
https://lucid.app/lucidchart/10f1098c-5c42-4b95-bc5c-b7efa0ea9f2f/edit?invitationId=inv_949f3552-1c51-49f4-9b2f-d0a3d1591922

Agent - Band tables
* Band CREATEs an account:
   * Name of band (String, not null)
   * Phone number (String, caters for leading zeros and country +44 etc)
   * Genre of music (pulldown from list, for agents to book for specific audiences)
   * Number of people in band (Integer)

* Agent CREATES an account:
   * Name of agent (String, not null)
   * Phone number (String, as above)
   * Backref to bands on signing

DELETE capability would be shown when the band decides on an agent, their account would be deleted so it wouldn't appear in the pool of talent.
This was a good idea at first but eventually was simpler to incorporate into CREATE band as a pulldown list when Agents object is populated.

The ERD can be found here:
https://lucid.app/lucidchart/10f1098c-5c42-4b95-bc5c-b7efa0ea9f2f/edit?invitationId=inv_949f3552-1c51-49f4-9b2f-d0a3d1591922

Our CI/CD pipeline was scaled down from what would be found in organisations. We used two virtual machines, one for Development/Jenkins, the 
other was used as the swarm manager to coordinate deployment of our frontend and backend containers:
https://1drv.ms/u/s!Aq2hJel0GwxW5xRUbdt3FoMUdIfG

## Project Planning
(https://github.com/echolocate/band-connect/projects/1)
### User stories
* As a band we want to add our details to available bands list so that we are visible to agents (CREATE)
* As a band we want to review our entry so that our information is correct (READ)
* As a band we want to be able to change details (band members/name) so that is information is always accurrate (UPDATE)
* As an band/agent we want the band entry deleted when signed so that the band is no longer available (DELETE)
* As an agent I want to add my details to available agents list so that I we are visible to bands (CREATE)
* As a agent I want to review/change my entry so that our information is correct (UPDATE)

## Testing
Using a bash shell script, Jenkins was used to coordinate the pretest (using pytest in a virtual environment),  in building of the front end and backend containers, pulling the source from GitHub via a webhook trigger, 
Unfortunately, my Jenkins installment on the Dev-Jenkins vm locked me out on the penultimate day. I managed to install it on my Deployment vm 
in order to show evidence of the test stage. I would like to get more coverage on the tests at a later date, if possible.


