#!/usr/bin/env bash

echo " ______          _  _      _  _                  _____    _______  _    _ "
echo "(____  \        (_)| |    | |(_)                (____ \  (_______)| |  | |"
echo " ____)  ) _   _  _ | |  _ | | _  ____    ____    _   \ \  _____   | |  | |"
echo "|  __  ( | | | || || | / || || ||  _ \  / _  |  | |   | ||  ___)   \ \/ / "
echo "| |__)  )| |_| || || |( (_| || || | | |( ( | |  | |__/ / | |_____   \  /  "
echo "|______/  \____||_||_| \____||_||_| |_| \_|| |  |_____/  |_______)   \/   "
echo "                                       (_____|                            "
echo "**************************************************************************"
echo "Configuration:"

docker-compose -f docker-compose.yml -f docker-compose-dev.yml config
docker-compose -f docker-compose.yml -f docker-compose-dev.yml ${1-up}
