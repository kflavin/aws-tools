#!/bin/bash
echo -n '"' ; sed ':again; N; $!b again; s/\\/\\\\/g; s/"/\\"/g; s/\n/\\n/g; s/$/\\n/;' $1 | tr -d '\n' ; echo '"'
