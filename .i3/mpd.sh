i3status --config ~/.i3/second.conf | while :
do
        read line
        playing=$(~/.i3/Mpd.py)
        # playing=$(mpc current)
        echo "$playing | $line" || exit 1
done
