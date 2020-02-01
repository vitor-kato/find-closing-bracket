#!/usr/bin/env bash

echo " ______          _  _      _  _                  ______  ______    _____   _____   "
echo "(____  \        (_)| |    | |(_)                (_____ \(_____ \  / ___ \ (____ \  "
echo " ____)  ) _   _  _ | |  _ | | _  ____    ____    _____) )_____) )| |   | | _   \ \ "
echo "|  __  ( | | | || || | / || || ||  _ \  / _  |  |  ____/(_____ ( | |   | || |   | |"
echo "| |__)  )| |_| || || |( (_| || || | | |( ( | |  | |           | || |___| || |__/ / "
echo "|______/  \____||_||_| \____||_||_| |_| \_|| |  |_|           |_| \_____/ |_____/  "
echo "                                       (_____|                                     "
echo "***********************************************************************************"
echo "Configuration:"

docker-compose -f docker-compose.yml -f docker-compose-prod.yml config
docker-compose -f docker-compose.yml -f docker-compose-prod.yml ${1-up --build}
