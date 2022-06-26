#!/bin/bash
sh drifters_sync.sh > ensemble_log.log && tail -f ensemble_log.log
