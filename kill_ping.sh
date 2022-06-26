#!/bin/bash
kill $(ps -aux | grep '[p]ing' | awk '{print $2}')