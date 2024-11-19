## Introduction
This a set of mock APIs generated using some static data and Python/Flask. OpenAPI specification (also called Swagger specification) is also available in the repo. There are two endpoints,

1. `/author`: takes a mandatory `authorid` url param to fetch an `author` object (`id` and `name`).
2. `/author-article`: takes a mandatory `authorid` url param to fetch one article written by this as an `article` object (`id`, `title` and `author_id`).

The APIs and the OpenAPI specification have been packed using docker compose, which you'll need to run these services. If you don't have them installed on your machine, head to [Docker's installation docs](https://docs.docker.com/compose/install/). The Python and Swagger services are hard coded to run on ports 5000 and 8080 respectively. If these ports are busy, please modify them in the docker-compose.yaml file.

## Running the services
1. Clone the repo:
   
   ```bash
   git clone https://github.com/dsandip/python-mock-api.git
   cd python-mock-api
   ```
2. Run the dockerized services  - `docker compose up`
