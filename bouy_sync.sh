#!/bin/bash
#sudo date --set="$(sshpass -p anliolr ssh pi@192.168.0.6 'date -u')"
sshpass -p anliolr ssh pi@192.168.0.6 sudo date -s @$(sudo date -u +"%s")
sshpass -p anliolr ssh pi@192.168.0.7 sudo date -s @$(sudo date -u +"%s")
sshpass -p anliolr ssh pi@192.168.0.8 sudo date -s @$(sudo date -u +"%s")
