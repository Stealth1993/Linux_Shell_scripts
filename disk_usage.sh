#!/bin/bash

THRESHOLD=90
USAGE=$(df / | tail -1 | awk '{print$5}' | sed 's/%//')

if [ "$USAGE" -gt "$THRESHOLD" ]; then
	echo "Disk space critical: ${USAGE}% used!" | mail -s "Disk Alert" admin@example.com

fi
