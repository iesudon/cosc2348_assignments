#!/bin/bash

#!/bin/bash
read INPUT
case "$INPUT" in
    #case 1
    "corpus") echo "Texas A&M University Corpus Christi" ;;
    #case 2
    "kingsville") echo "Texas A&M University Kingsville" ;;
    #case 3
    "commerce") echo "Texas A&M University Commerce" ;;
    "*") echo "Texas A&M University";;
esac