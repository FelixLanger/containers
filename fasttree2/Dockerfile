# FastTree2 Dockerfile
FROM ubuntu:20.04

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gcc \
    make

# Set the working directory
WORKDIR /usr/local/bin

# Download and compile FastTree
RUN wget http://www.microbesonline.org/fasttree/FastTree.c &&\
    gcc -O3 -finline-functions -funroll-loops -Wall -o FastTree FastTree.c -lm &&\
    rm FastTree.c

# Set FastTree as the default command
ENTRYPOINT ["FastTree"]
