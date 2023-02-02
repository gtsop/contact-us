#!/usr/bin/env sh
if [ "$1" == "--watch" ]; then
    ptw --runner "pytest --testmon"
else
    pytest
fi