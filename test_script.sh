#!/bin/bash

cd Prize_Generator
cd random_letters
pytest --cov=application 
cd .. && cd random_numbers
pytest --cov=application
