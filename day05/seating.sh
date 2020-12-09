#!/bin/bash

cat input | tr FBLR 0101 | xargs -i  bash -c 'echo "$((2#{}))"'  | sort -n | tail -1
