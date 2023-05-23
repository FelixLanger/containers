#!/usr/bin/env python3

import os

def create_directory_and_workflow():
    tool_name = input("Enter the name of the tool: ")

    # Create the directory
    directory_path = f"./{tool_name}"
    os.makedirs(directory_path, exist_ok=True)

    # Create the Dockerfile
    with open(f"{directory_path}/Dockerfile", "w") as f:
        pass  # An empty Dockerfile is created

    # Create the workflow YAML
    workflow = f"""name: BUILD {tool_name.upper()} CONTAINER

on:
  push:
    paths:
    - '{tool_name}/**'
    branches:
    - main
jobs:
  push_to_registry:
    name: Push Docker image to Docker Hub
    runs-on: ubuntu-latest
    steps:
      - name: Check out the repo
        uses: actions/checkout@v2

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Login to DockerHub
        uses: docker/login-action@v2 
        with:
          username: ${{{{ secrets.DOCKERHUB_USERNAME }}}}
          password: ${{{{ secrets.DOCKERHUB_TOKEN }}}}

      - name: Build and push
        uses: docker/build-push-action@v2
        with:
          context: ./{tool_name}
          push: true
          tags: ${{{{ secrets.DOCKERHUB_USERNAME }}}}/{tool_name.lower()}:latest
    """

    # Save the workflow to a .yml file
    with open(f".github/workflows/docker-build-push-{tool_name.upper()}.yml", "w") as f:
        f.write(workflow)

if __name__ == "__main__":
    create_directory_and_workflow()
