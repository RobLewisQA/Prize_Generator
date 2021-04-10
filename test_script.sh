#!/bin/bash

cd Prize_Generator

pytest random_letters --cov=application 

pytest random_numbers --cov=application

pytest back-end --cov=application
