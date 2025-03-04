#!/bin/bash

SERVICE=httpd

if ! systemctl is-active --quiet $SERVICE; then
	echo "$SERVICE is not running. Restarting..."
	sudo systemctl restart $SERVICE

else
	echo "$SERVICE is running normally."

fi
