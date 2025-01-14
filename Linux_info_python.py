#!/usr/bin/env python
import os
import subprocess
import platform

# Get the current user name
user = os.getlogin()
print("Current user:", user)

# Get the current working directory
pwd = os.getcwd()
print("Current working directory:", pwd)

# Get the output of ls -lh command
output = subprocess.check_output(['ls', '-lh'])
print("Output of ls -lh:")
print(output)

# Get the hostname of the system
hostname = platform.node()
print("Hostname:", hostname)

# Get the system awake time in seconds
awake_time = subprocess.check_output(['cat', '/proc/uptime']).split()[0]
print("System awake time:", awake_time, "seconds")

# Get the OS version
os_version = platform.platform()
print("OS version:", os_version)

# Get the kernel version
kernel_version = platform.release()
print("Kernel version:", kernel_version)

# Get the update status
update_status = subprocess.check_output(['apt', 'list', '--upgradable'])
print("Update status:")
print(update_status)

# Save the output to a text file
with open('info.txt', 'w') as f:
    f.write(f"Current user: {user}\n")
    f.write(f"Current working directory: {pwd}\n")
    f.write(f"Output of ls -lh:\n{output}\n")
    f.write(f"Hostname: {hostname}\n")
    f.write(f"System awake time: {awake_time} seconds\n")
    f.write(f"OS version: {os_version}\n")
    f.write(f"Kernel version: {kernel_version}\n")
    f.write(f"Update status:\n{update_status}\n")

print("The output has been saved to info.txt")