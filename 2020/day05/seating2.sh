#!/bin/bash

TMP=$(tempfile) || exit
trap "rm -f -- '$TMP'" EXIT

cat input | tr FBLR 0101 | xargs -i  bash -c 'echo "$((2#{}))"'  | sort -n > $TMP
HIGH=$(tail -1 $TMP)
LOW=$(head -1 $TMP)

TMP2=$(tempfile) || exit
trap "rm -f -- '$TMP2'" EXIT
echo $LOW $HIGH
seq $LOW $HIGH > $TMP2

echo $TMP
echo $TMP2

diff $TMP $TMP2

rm -f -- "$TMP" "$TMP2"
trap - EXIT
exit
