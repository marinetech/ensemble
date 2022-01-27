#!/bin/bash
sh bouy_sync.sh > ensemble_log.log && tail -f ensemble_log.log
