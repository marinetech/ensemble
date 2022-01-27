#!/bin/bash
sshpass -p anliolr ssh pi@192.168.0.6 sh /home/pi/ensemble/kill_ping.sh &
sshpass -p anliolr ssh pi@192.168.0.7 sh /home/pi/ensemble/kill_ping.sh &
sshpass -p anliolr ssh pi@192.168.0.8 sh /home/pi/ensemble/kill_ping.sh &
#ps aux  |  grep -i 'bouy_sync' |  awk '{print $2}'  |  xargs sudo kill -9
#kill $(ps -aux | grep '[b]ouy_sync' | awk '{print $2}')
