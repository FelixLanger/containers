FROM python:3.11

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install the necessary python libraries for plotting
RUN pip install pandas plotly numpy seaborn matplotlib

# Create a working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
