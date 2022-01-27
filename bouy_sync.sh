#!/bin/bash
sshpass -p anliolr ssh pi@192.168.0.6 sudo date -s @$(sudo date -u +"%s")
sshpass -p anliolr ssh pi@192.168.0.7 sudo date -s @$(sudo date -u +"%s")
sshpass -p anliolr ssh pi@192.168.0.8 sudo date -s @$(sudo date -u +"%s")
sshpass -p anliolr ssh pi@192.168.0.6 sh /home/pi/ensemble/ping_timing.sh &
sshpass -p anliolr ssh pi@192.168.0.7 sh /home/pi/ensemble/ping_timing.sh &
sshpass -p anliolr ssh pi@192.168.0.8 sh /home/pi/ensemble/ping_timing.sh &
