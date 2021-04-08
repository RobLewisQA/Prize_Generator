# Prize Project
## Application Overview
> Prize Project is a web application for 




## Setup
> The source code for the Prize Project web application can be cloned from [this Github repository](https://github.com/RobLewisQA/Prize_Project). In order to run the application on Linux Ubuntu 18.04 on your localhost port, ensure that you have Python 3.6 or higher installed, as well as the python installer package, pip3. The following commands should be input in order into your Linux terminal:
1. git init
2. git clone https://github.com/RobLewisQA/Practical_Project
2. (cd Prize_Project)
3. sh docker_installation.sh
4. docker-compose build
5. docker-compose up -d  

## Technologies
#### Cloud Server Host:
> This web application was designed using a cloud-hosted (GCP) compute machine developed on a Linux Ubuntu 20.10 bootdisk - the most recent with long-term support at the time of writing, and has been tested on Ubuntu 18.04. Earlier or later versions of Ubuntu may cause the app to behave unexpectedly, depending on support for versions of the app's dependencies.  
#### Database format:
> The database is a MySQL5.7 single table database image within a Docker container. The app source-code uses SQLalchemy for reading from and writing to the database using python commands.
#### Frontend script:
> The application uses the Flask web-development framework to allow python statements to manage HTML output for the URI routes specified in the routes file. HTML forms are used for the frontend to send post and get requests to the database in the backend. The html templates are constructed using Jinja2 to allow the use of variables in templating construction. The primary modules within Flask used for frontend purposes include render_template, request, url_for and jsonify. 
#### Scripting software:
> The logic for the random number generator, random letter generator and the backend data handling is scripted using python 3.6. The python requests library, in conjunction with the Flask API is used to send JSON data to specified routes. The Dockerfiles are scripted in GO, the docker-compose.yaml and Ansible scripts use the YAML language and the Jenkinsfile uses Declarative Pipeline (based on the Groovy syntax).
#### Testing software:
> This application was tested using the flask-testing, unittest, pytest, pytest-cov python libraries. The testing thoughouly interrogates the app's logic and configuration, using mock API requests and the SQLite database engine for data-submission testing. The coverage of testing is [INSERT HERE]% altogether.
> To replicate the testing, simply run...
#### Deployment software:
> Prize Project was designed for containerised deployment across 4 virtual machines - each machine's name and role is specified in the Ansible inventory.yaml file, so these must be followed or changed appropriately for Ansible to connect to them. Docker is the containerisation tool used for this application, and Ansible is used with Jenkins to initialise a swarm of a manager node, a worker node and an Nginx node acting as the reverse proxy as well as a load balancer. It is recommended that only the Nginx node be accessible to HTTP traffic - the script design is based on ports 5000, 5001, 5002 and 5003 being inaccessibile to public requests.
>Continuous Deployment utilises a Jenkins pipeline to support automated deployment using Git Webhooks, so that a push to a specified branch of the repository intiates a rebuild of the app on the new source code without bringing the web-app down in the meanwhile. The Jenkins pipeline also pushes the images of containers to a Docker Hub repository before initiating the swarm deployment. This saves build time where the image already exists and can be pulled down from Docker Hub rather than rebuilt each time.
#### Continous Integration and Version Control:
> The source code for this application is maintained in a Github repository accessible [here](https://github.com/RobLewisQA/Prize_Project), and can be conncted to Jenkins for automatic continuous integration and deployment.

## Database Entity Relationship Diagram
> The database for Prize is composed of 2 tables: 
![chart](Tuckshop_ERD.PNG)

## Risk Assessment
Description | Evaluation | Likelihood | Impact Level | Responsibility | Response | Control Mearues
| --- | --- | --- | --- | --- | --- | --- |
Application's virtual compute machine goes down | Application goes offline | Low | High | GCP | Spin up a new vm instance either in GCP or an alternative cloud provider and clone the Github repo to integrate with Jenkins | Keep an up-to-date source code on Github
Application's virtual MySQL machine goes down | Application becomes unusable | Low | High | GCP | Spin up a new vm instance in GCP and update the configurations with SQLAlchemy and the virtual compute machine | Keep a backup database
The Python language is updated to a new version | The application may not run if Flask and SQLAlchemy are not updated for compatibility | Medium | Medium | Developers | Run the application on Python 3 and phase in an updated version in CI | Keep a robust Github repo so that the source code can be continuously improved and use Jenkins to manage the integration and deployment
Versions of libraries are updated and compatability issues are not mitigated | Some aspects of the application may fail | Medium | High | Developers | Update the requirements.txt to specify the exact versions required | Keep track of planned updates to key libraries, and specify the versions of some of the key libraries required for function
The port that the application runs on changes | The app stops working | Low | High | CI Engineers/Operators | Update the firewall settings in the cloud provider to allow a different port access | Use Jenkins to manage continuous integration in the app, and notify when there are launch issues

## Development workflow:
>To see a kanban Trello board of the development process workflow, click [here](https://trello.com/b/h1v0LX39/lottery)

## References:
##### r1 - https://appfleet.com/blog/building-docker-images-to-docker-hub-using-jenkins-pipelines/ - using jenkins with dockerhub
##### r2 - https://www.blazemeter.com/blog/how-to-integrate-your-github-repository-to-your-jenkins-project