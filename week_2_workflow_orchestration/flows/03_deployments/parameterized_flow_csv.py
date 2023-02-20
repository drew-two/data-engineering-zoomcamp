from pathlib import Path
import pandas as pd
from datetime import timedelta
import urllib.request 

from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect.tasks import task_input_hash

@task(retries=3)
def fetch(dataset_path: Path, dataset_file: str, dataset_url: str) -> Path:
    """Read taxi data from web into pandas DataFrame"""
    dataset_path.mkdir(parents=True, exist_ok=True)
    dataset_path = dataset_path / f"{dataset_file}.csv.gz"

    local_filename, _ = urllib.request.urlretrieve(dataset_url, dataset_path)
    return Path(local_filename)

@task()
def write_gcs(path: Path) -> None:
    """Uploading local Parquet file to GCS"""
    gcp_block = GcsBucket.load("zoom-gcs")
    gcp_block.upload_from_path(
        from_path = path,
        to_path = path
    )
    return

@flow()
def etl_web_to_gcs(year: int, month: int, color: str) -> None:
    """The main ETL function"""
    dataset_path = Path(f"data/{color}/")
    dataset_file = f"{color}_tripdata_{year}-{month:02}"
    dataset_url= f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{dataset_file}.csv.gz"

    print(dataset_url)
    path = fetch(dataset_path, dataset_file, dataset_url)
    write_gcs(path)

@flow()
def etl_parent_flow(
    months: list[int] = [1, 2], year: int = 2021, color: str = "yellow"
):
    for month in months:
        etl_web_to_gcs(year, month, color)

if __name__ == '__main__':
    color = "yellow"
    months = [1, 2, 3]
    year = 2021
    etl_parent_flow(months, year, color)