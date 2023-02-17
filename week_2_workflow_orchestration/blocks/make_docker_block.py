from prefect.infrastructure.docker import DockerContainer

# alternative to creating DockerContainer block in the UI
docker_block = DockerContainer(
    image = "drewsg/prefect:zoom", # image name
    image_pull_policy="ALWAYS",
    auto_remove=True
)

docker_block.save("zoom", overwrite=True)