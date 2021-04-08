# Lottery
## Application Overview
> Lottery is a web application for 




## Setup
> The source code for the Lottery web application can be cloned from [this Github repository](https://github.com/RobLewisQA/Practical_Project). In order to run the application on Linux Ubuntu 18.04 on your localhost port, ensure that you have Python 3.6 or higher installed, as well as the python installer package, pip3. The following commands should be input in order into your Linux terminal:
1. git init
2. git clone https://github.com/RobLewisQA/Practical_Project
2. (cd Lottery_Project)
3. sh docker_installation.sh
4. docker-compose build
5. docker-compose up -d  

## Technologies
#### Cloud Server Host:
> This web application was designed using the Google Cloud Platform to host a compute machine developed on a Linux Ubuntu 18.04 bootdisk.
#### Database format:
> The database is a MySQL 5.7 relational database image within a Docker container. The database is integrated with SQLalchemy for reading from and writing to the database using python commands.
#### Frontend script:
> The application uses the Flask web-development framework to allow python statements to manage HTML output for the URI routes specified in the routes file. HTML forms are used for the frontend to send post and get requests to the database in the backend.
#### Testing software:
> This application was tested using the flask-testing, pytest and pytest-cov python libraries. The unit and configuration testing thoughouly interrogates the read, create, update and delete functions, with coverage of 83% of the entire application.
> To replicate the testing, simply run steps 1. and 2. of the setup instructions, followed by: *pytest --cov=application*
#### Deployment software:
> The application was designed and tested for deployment using Jenkins to automate Linux command execution of virtual environment generation, dependencies installation and Gunicorn web-deployment. 
#### Continous Integration and Version Control:
> The source code for this application is maintained in a Github repository accessible [here](https://github.com/RobLewisQA/Practical_Project), and can be conncted to Jenkins for automatic continuous integration and deployment.

## Database Entity Relationship Diagram
> The database for Lottery is composed of 2 tables: 
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