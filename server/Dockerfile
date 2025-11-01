###############################################################################
# Base image for generating the requirements file
###############################################################################
FROM python:3.14-slim AS requirements

# Install Poetry for managing the Python dependencies
RUN python -m pip install pip~=24.0.0 \
    --upgrade --no-cache-dir --disable-pip-version-check --no-compile \
    && python -m pip install poetry~=1.0 \
    --no-cache-dir --disable-pip-version-check --no-compile

# Set the working directory to generate the "requirements.txt" file inside
WORKDIR /tmp/remington

# Copy the lockfiles and configuration files
COPY pyproject.toml poetry.lock ./

# Generate the "requirements.txt" file
RUN poetry export --output=requirements.txt --only=main

###############################################################################
# Stage for the development runtime of the application
###############################################################################
FROM python:3.14-slim-bookworm AS dev

RUN apt-get update \
    && apt-get upgrade --yes \
    && apt-get clean \
    && rm --recursive --force /var/lib/apt/lists/*

# Set the working directory to make the linter happy
WORKDIR /server

# Copy the "requirements.txt" file from the previous stage
COPY --from=requirements /tmp/remington/requirements.txt .

# Install and cache the dependencies
RUN --mount=type=cache,target=/root/.cache \
    python -m pip install pip~=24.0.0 --upgrade --no-cache-dir \
    --disable-pip-version-check --no-compile && \
    python -m pip install --requirement "requirements.txt" \
    --require-hashes --no-cache-dir --disable-pip-version-check \
    --no-compile --no-warn-script-location && \
    rm --force "requirements.txt"

# Copy the source code
COPY . .

# Expose the port to access the API service
EXPOSE 8000

# Invoke the entrypoint to start the service
CMD [ "python", "-m", "src.main" ]
