#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
for f in *.hda
do
    if [ -d $f ]
    then
        if hotl -l $f /tmp/$f
        then
            rm -rf $DIR/$f
            mv /tmp/$f $DIR
        fi
    fi
done