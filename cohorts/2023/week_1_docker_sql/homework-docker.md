# Docker/SQL Homework

Refers to [Cohort 2023 Week 1](../cohorts/2023/week_1_docker_sql/).

## Question 1. Knowing Docker tags

Run the command to get information on Docker

docker --help

Now run the command to get help on the "docker build" command

Which tag has the following text? - Write the image ID to the file

* --imageid string
* --iidfile string
* --idimage string
* --idfile string

### Answer
--iidfile string

## Question 2. Understanding docker first run
Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash. Now check the python modules that are installed ( use pip list). How many python packages/modules are installed?

* 1
* 6
* 3
* 7

### Answer
```
$ docker run --rm -it --entrypoint bash python:3.9
$ pip list
```

**3** packages

## Prepare Postgres
Run Postgres and load data as shown in the videos We'll use the green taxi trips from January 2019:

wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz

You will also need the dataset with zones:

wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)