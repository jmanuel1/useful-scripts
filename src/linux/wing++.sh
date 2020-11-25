#!/bin/bash

# Meant to be used with /src/windows/g++.cmd.
# See https://github.com/tvincent056/linter-gcc2/wiki/Using-linter-gcc2-with-Windows-Subsystem-for-Linux-(WSL).
# Use xargs because what's on that Wiki doesn't work if an argument has spaces in it.

# FIXME: Support drives other than C:.
inputArgs=$(echo "$@" | sed 's/C:/\/mnt\/c/g' | sed 's/\\/\//g')

output=$(echo ${inputArgs} | xargs g++ 2>&1)
output=$(echo "$output" | sed 's/\/mnt\/c/C:/g' | sed 's/\//\\/g')
(>&2 echo "$output")
