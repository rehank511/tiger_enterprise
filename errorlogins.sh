#!/bin/bash
echo "Examining file $1"
if file $1 | grep -q compressed;then
   echo "File is compressed acrchive"
   tempFile=/tmp/tmp.log
   echo "decompressing file to temp location: $tempFile"
   gzip -dk < $1 > /tmp/tmp.log
else
   tempFile=$1
fi
awk '($9 ~ /invalid/)' $tempFile | awk '{print $1 " " $2 " " $3 " " $11 " " $12}' | sed '1!G;h;$!d'
if file $1 | grep -q compressed;then
   rm $tempFile
fi
