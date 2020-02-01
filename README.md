# Find Closing Bracket APP

Django-React App that given an expression with brackets E.g. [AB] and a bracket index, returns the matching closing bracket to the user

Input:
String = [AB], Index = 0

Output: 4

## Getting Started

Assuming you have docker installed, you can easily run the app using `docker-compose up`

First you only need to fill in the `.env.example` file located in the backend of the project

### Prerequisites

- A working installation of docker and docker-composer

### Installing

Clone the repo

```sh
git clone https://github.com/vitor-kato/find-closing-bracket.git
cd find-closing-bracket
```

Fill the `.env.example` or just copy it as is

```sh
cp backend/.env.example backend/find_closing_bracket/.env
```

Fire it up

```sh
./build-dev.sh
```

When docker finishes building the images, head to your browser and enter the address

```sh
http://0.0.0.0:8081/
```

Then enter an string with some brackets like `[ABC[23]][89]`, and the index of the bracket that you want to find the matching closing bracket.

## Roadmap

- Migrate from sqlite
- Better comply to 12-factor app
- Add authentication
- Async calls between services
- Better pagination overall page
- ?
