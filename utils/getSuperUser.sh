#!/bin/bash
#
# Script for retrieving Super user authentication token.
# It's generating on each TC boot.
# New token is being appended into the file.
# Usage: `sh utils/getSuperUser.sh ~/JetBrains/TeamCity/`
#  where `~/JetBrains/TeamCity/`
#  is a parameter that determines TeamCity location.
#
# Script should be run:
# - when TC is up and running AND
# - before executing tests

OUTPUT_FILE="superUser"
if [ -f "$OUTPUT_FILE" ]; then
    rm $OUTPUT_FILE
fi
grep -oP '(?<=Super user authentication token: )\d+' $1logs/teamcity-server.log | tail -1 >> $OUTPUT_FILE
