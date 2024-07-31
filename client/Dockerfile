###############################################################################
# Stage to generate the dependency list
###############################################################################
FROM node:22-bookworm-slim AS dev-dependencies

# Update the environment and install the "pnpm" package manager
RUN apt-get update \
    && apt-get upgrade --yes \
    && apt-get clean \
    && rm --recursive --force /var/lib/apt/lists/* \
    && npm install --global pnpm@latest

# Set the working directory to a temporary throwaway location
WORKDIR /tmp/remington

# Copy the configuration files to install the necessary dependencies
COPY ./package.json ./pnpm-lock.yaml ./

# Install and generate the dependency list
RUN pnpm install

###############################################################################
# Stage to run the development server of the project
###############################################################################
FROM node:22-bookworm-slim AS dev

# Update the environment and install the "pnpm" package manager
RUN apt-get update \
    && apt-get upgrade --yes \
    && apt-get clean \
    && rm --recursive --force /var/lib/apt/lists/* \
    && npm install --global pnpm@latest

# Set the working directory for the runtime environment
WORKDIR /client

# Copy the dependencies
COPY --from=dev-dependencies /tmp/remington/node_modules ./node_modules

# Copy the source code from the host to the container
COPY ./src ./src

COPY ./package.json ./nuxt.config.ts ./tsconfig.json eslint.config.js ./

# Expose the port outside the container
EXPOSE 3000

# Temporarily disable the healthcheck especially since its only a dev runtime
HEALTHCHECK NONE

# Spin up the development server
CMD [ "pnpm", "run", "dev" ]
