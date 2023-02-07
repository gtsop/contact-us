#!/usr/bin/env sh
if [ "$1" == "--watch" ]; then
    ptw --runner "pytest --testmon -v "
else
    pytest --capture=no --log-cli-level=DEBUG
fi