#!/bin/bash
flag=true
while true; do
  time=$(date +%S)
  if [ "$time" -eq 01 ] ; then
    python3 /home/pi/nm3-python-driver/ensemble.py
  fi
  sleep 1
done
