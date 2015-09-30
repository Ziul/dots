#!/bin/sh

i3status --config ~/.i3/config_second.conf | while :
do
	read line
	mpd=$(ncmpcpp --now-playing)
	echo "$mpd | $line" || exit 1
done

