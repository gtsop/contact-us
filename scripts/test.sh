#!/usr/bin/env sh
POSITIONAL_ARGS=()

while [[ $# -gt 0 ]]; do
  case $1 in
    -l|--log)
      SHOW_LOGS="YES"
      shift
      ;;
    -w|--watch)
      WATCH_MODE="YES"
      shift
      ;;
    -*|--*)
      echo "Unknown option $1"
      exit 1
      ;;
    *)
      POSITIONAL_ARGS+=("$1") # save positional arg
      shift # past argument
      ;;
  esac
done

set -- "${POSITIONAL_ARGS[@]}" # restore positional parameters

PYTEST_COMMAND="pytest"

if [ "$SHOW_LOGS" == "YES" ]; then
    PYTEST_COMMAND="$PYTEST_COMMAND --capture=no --log-cli-level=DEBUG"
fi

if [ "$WATCH_MODE" == "YES" ]; then
    PYTEST_COMMAND="$PYTEST_COMMAND --testmon -v "
    ptw --runner "$PYTEST_COMMAND"
else
    $PYTEST_COMMAND
fi