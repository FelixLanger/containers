FROM debian:latest

# Set environment variables
ENV HMMER_VERSION="3.3.2"

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Download and unpack HMMER
RUN wget http://eddylab.org/software/hmmer/hmmer-${HMMER_VERSION}.tar.gz && \
    tar -xvf hmmer-${HMMER_VERSION}.tar.gz && \
    rm hmmer-${HMMER_VERSION}.tar.gz

# Install HMMER
WORKDIR hmmer-${HMMER_VERSION}
RUN ./configure && \
    make && \
    make install

# Copy esl-* programs to /usr/local/bin
RUN cp easel/miniapps/esl-* /usr/local/bin/

# Set the working directory back to root
WORKDIR /

# Clean up the HMMER directory
RUN rm -rf hmmer-${HMMER_VERSION}

# Test the installation
RUN which hmmsearch && \
    which esl-alimanip
