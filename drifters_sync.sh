#!/bin/bash
sshpass -p anliolr ssh pi@drifter-1 sudo date -s @$(sudo date -u +"%s")
sshpass -p anliolr ssh pi@drifter-2 sudo date -s @$(sudo date -u +"%s")
sshpass -p anliolr ssh pi@drifter-3 sudo date -s @$(sudo date -u +"%s")
sshpass -p anliolr ssh pi@drifter-4 sudo date -s @$(sudo date -u +"%s")

sshpass -p anliolr ssh pi@drifter-1 sh /home/pi/ensemble/ping_timing.sh &
sshpass -p anliolr ssh pi@drifter-2 sh /home/pi/ensemble/ping_timing.sh &
sshpass -p anliolr ssh pi@drifter-3 sh /home/pi/ensemble/ping_timing.sh &
sshpass -p anliolr ssh pi@drifter-4 sh /home/pi/ensemble/ping_timing.sh &
