#!/bin/bash
#
# Script for retrieving Super user authentication token.
# It's generating on each TC boot.
# New token is being appended into the file.
# Usage: `sh ./config/getSuperUser.sh ~/JetBrains/TeamCity/`
#  where `~/JetBrains/TeamCity/`
#  is a parameter that determines TeamCity location.
#
# Script should be run:
# - when TC is up and running AND
# - before executing tests

OUTPUT_FILE="superUser"
if [ -f "./config/$OUTPUT_FILE" ]; then
    rm ./config/$OUTPUT_FILE
fi

if ! [ $1 ]; then
    echo "Path for TC project not provided. Try:"
    echo "sh ./config/getSuperUser.sh ~/JetBrains/TeamCity/"
    exit 1
fi

grep -oP '(?<=Super user authentication token: )\d+' $1logs/teamcity-server.log | tail -1 >> ./config/$OUTPUT_FILE