#!/bin/bash

IMAGE_DIR=$1

for imgfile in `find $IMAGE_DIR -iname "*.dcm"`; do
    python main.py $imgfile
done
