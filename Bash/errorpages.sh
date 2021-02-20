#!/bin/bash
echo "Examining file $1"
if file $1 | grep -q compressed;then
   echo "File is compressed"
   tempFile=/tmp/tmp.log
   echo "decompressing it to temp location: $tempFile"
   gzip -dk < $1 > /tmp/tmp.log
else
   tempFile=$1
fi
awk '($9 ~ /404/)' $tempFile | awk '{print $7 " " $9}' | sort | uniq -c | sort -rn
if file $1 | grep -q compressed;then
   rm $tempFile
fi
