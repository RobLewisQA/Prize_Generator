#!/bin/bash
cd Prize_Generator


sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install requests_mock

pytest random_letters --cov=application 
pytest random_numbers --cov=application
pytest back-end --cov=application
pytest frontend --cov=application
