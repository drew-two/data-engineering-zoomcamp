# Week 4 Homework

### Question 1: 

**What is the count of records in the model fact_trips after running all models with the test run variable disabled and filtering for 2019 and 2020 data only (pickup datetime)?** 

You'll need to have completed the ["Build the first dbt models"](https://www.youtube.com/watch?v=UVI30Vxzd6c) video and have been able to run the models via the CLI. 
You should find the views and models for querying in your DWH.

- 41648442
- 51648442
- 61648442
- 71648442

**Ans:** 61602988
```
SELECT COUNT(*)
FROM `dtc-de-377105.production.fact_trips`
WHERE 
  EXTRACT(YEAR FROM pickup_datetime) = 2019
  or
  EXTRACT(YEAR FROM pickup_datetime) = 2020;
```

### Question 2: 

**What is the distribution between service type filtering by years 2019 and 2020 data as done in the videos?**

You will need to complete "Visualising the data" videos, either using [google data studio](https://www.youtube.com/watch?v=39nLTs74A3E) or [metabase](https://www.youtube.com/watch?v=BnLkrA7a6gM). 

- 89.9/10.1
- 94/6
- 76.3/23.7
- 99.1/0.9

**Ans:** 89.8/10.2

Report: https://lookerstudio.google.com/reporting/2ba9763f-69d8-4b5e-8e7a-cfc3486808d9

### Question 3: 

**What is the count of records in the model stg_fhv_tripdata after running all models with the test run variable disabled (:false)?**  

Create a staging model for the fhv data for 2019 and do not add a deduplication step. Run it via the CLI without limits (is_test_run: false).
Filter records with pickup time in year 2019.

- 33244696
- 43244696
- 53244696
- 63244696

**Ans:** 43244696
```
SELECT COUNT(*)
FROM `dtc-de-377105.dbt_akatoch.stg_fhv_tripdata`
WHERE EXTRACT(YEAR FROM pickup_datetime) = 2019;
```

### Question 4: 

**What is the count of records in the model fact_fhv_trips after running all dependencies with the test run variable disabled (:false)?**  

Create a core model for the stg_fhv_tripdata joining with dim_zones.
Similar to what we've done in fact_trips, keep only records with known pickup and dropoff locations entries for pickup and dropoff locations. 
Run it via the CLI without limits (is_test_run: false) and filter records with pickup time in year 2019.

- 12998722
- 22998722
- 32998722
- 42998722

**Ans:** 22998722
```
SELECT COUNT(*)
FROM `dtc-de-377105.dbt_akatoch.fact_fhv_trips`
WHERE EXTRACT(YEAR FROM pickup_datetime) = 2019;
```

### Question 5: 

**What is the month with the biggest amount of rides after building a tile for the fact_fhv_trips table?**

Create a dashboard with some tiles that you find interesting to explore the data. One tile should show the amount of trips per month, as done in the videos for fact_trips, based on the fact_fhv_trips table.

- March
- April
- January
- December

**Ans:** January

Dashboard URL: https://lookerstudio.google.com/reporting/411a0af3-0417-451e-a9ea-95c672ecadd4