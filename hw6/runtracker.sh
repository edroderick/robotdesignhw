#!/bin/bash

#open ACH channel and run python scripts

COG_CHAN='cog-chan'

MakeACH(){
  ach -1 -C $COG_CHAN -m 30 -n 30000
  sudo chmod 777 /dev/shm/achshm-*
}

KillAll(){
  sudo rm -r /dev/shm/achshm*
}

case "$1" in
  'make' )
    MakeACH
  ;;
  'kill' )
    KillAll
  ;;
  *)
    MakeACH
    #call python scripts
    python colorTracker.py
  ;;
esac

exit 0
#END
