# README #

To run,
Simply checkout the project and do execute following:

#!/bin/bash -e
docker-compose build
docker-compose run awsutil python app/ebsversions.py remove_ebs_versions 3
docker-compose down


### What is this repository for? ###

Docker and docker-compose based python project. It is used to delete all ebs versions from aws but keep a few for each application

### How do I get set up? ###

* Should have valid aws account
* Should have installed aws cli, docker and compose on machine where you are running this code.
* Python should be installed

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact