# Commands for this chapter

Just apply to my environment.

## Postgres
```
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v ~/data-engineering-zoomcamp/week_1_basics_n_setup/2_docker_sql/ny_taxi_postgres_data/:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13
```

`pgcli -h localhost -d ny_taxi -u root`

## pgAdmin
```
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network pg-network \
    --name pgadmin \
dpage/pgadmin4
```

## Pipeline Image
```
URL="http://172.25.8.156:8000/yellow_tripdata_2021-01.csv"

docker run -it \
    --network=pg-network \
    taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_data \
    --url=${URL}
```

## Terraform Project

1. `terraform init`
2. `terraform plan`
3. `terraform apply`
4. `terraform destroy`

## Remote SSH
Got Remote SSH working with the following in User settings JSON:
```
"remote.SSH.path": "C:/Users/andre/ssh.bat",
```
- This file contains:
    ```
    C:\Windows\system32\wsl.exe ssh %*
    ```
- Which uses the WSL SSH directly as well as the default user's .ssh configuration