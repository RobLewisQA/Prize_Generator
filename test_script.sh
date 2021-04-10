#!/bin/bash

pip3 install requests_mock
cd Prize_Generator

pytest random_letters --cov=application 
pytest random_numbers --cov=application
pytest back-end --cov=application
pytest frontend --cov=application


