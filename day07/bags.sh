#!/bin/bash

INIT="shiny gold"

if [ -z "$1" ]; then
  rm results
  touch results
else
  INIT="$1"
fi
echo $INIT

LINES=$(grep "$INIT bags\?[\\.,]" input | cut -d' ' -f1-2 | tee -a results)

if [ -z "$LINES" ]; then
  echo "exiting"
  exit
fi

while IFS= read line; do
  ./bags.sh "$line"
done <<< "$LINES"


if [ -z "$1" ] ; then
  sort -u results | wc -l
fi
