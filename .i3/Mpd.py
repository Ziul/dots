#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 et tw=79:

from __future__ import unicode_literals

import sys
import ctypes


[MPD_TAG_UNKNOWN, MPD_TAG_ARTIST, MPD_TAG_ALBUM, MPD_TAG_ALBUM_ARTIST, MPD_TAG_TITLE, MPD_TAG_TRACK, MPD_TAG_NAME, MPD_TAG_GENRE, MPD_TAG_DATE, MPD_TAG_COMPOSER, MPD_TAG_PERFORMER, MPD_TAG_COMMENT, MPD_TAG_DISC, MPD_TAG_MUSICBRAINZ_ARTISTID, MPD_TAG_MUSICBRAINZ_ALBUMID, MPD_TAG_MUSICBRAINZ_ALBUMARTISTID, MPD_TAG_MUSICBRAINZ_TRACKID, MPD_TAG_COUNT
 ] = map(ctypes.c_int, range(-1, 17))


class Mpd(object):

    """
    Docstring for Mpd
    """

    def __init__(self, *args, **kwargs):
        """
        """
        super(Mpd, self).__init__(*args, **kwargs)

        self.libmpdclient = ctypes.CDLL("libmpdclient.so.2")
        self.mpd_connection = None

    def connect(self):
        self.mpd_connection = self.libmpdclient.mpd_connection_new \
            (None  # Default host
             , 0    # Default port
             , 0    # Default timeout
             )

    def disconnect(self):
        if None is not self.mpd_connection:
            self.libmpdclient.mpd_connection_free(self.mpd_connection)
            self.mpd_connection = None

    def is_connected(self):
        return None is not self.mpd_connection

    def __del__(self):
        self.disconnect()

    def status(self):
        if not self.is_connected():
            self.connect()

            if not self.is_connected():
                return "Mpd: Out of memory"

        connect_error = \
            self.libmpdclient.mpd_connection_get_error(self.mpd_connection)

        if 0 != connect_error:
            self.disconnect()
            return "Mpd: Not running"

        mpd_status = self.libmpdclient.mpd_run_status(self.mpd_connection)

        if 0 == mpd_status:
            return "Mpd: Unknown"

        state = self.libmpdclient.mpd_status_get_state(mpd_status)
        song_id = self.libmpdclient.mpd_status_get_song_id(mpd_status)
        volume = self.libmpdclient.mpd_status_get_volume(mpd_status)

        self.libmpdclient.mpd_status_free(mpd_status)

        state_string = None

        if 0 == state:
            state_string = "(Unknown)"  # Unknown
        elif 1 == state:
            state_string = "■"         # Stopped
        elif 2 == state:
            state_string = "▶"         # Playing
        elif 3 == state:
            state_string = "▮▮"        # Paused

        song_string = ""

        if -1 == song_id:
            song_string = "Mpd: No song"
        else:
            song = self.libmpdclient.mpd_run_get_queue_song_id(
                self.mpd_connection, song_id)

            self.libmpdclient.mpd_song_get_tag.restype = ctypes.c_char_p

            def tag_to_str(tag):
                tag_value = self.libmpdclient.mpd_song_get_tag(song, tag, 0)
                if sys.version < '3':
                    return unicode(tag_value, "utf-8") if None != tag_value else ""
                else:
                    return str(tag_value, "utf-8") if None != tag_value else ""

            song_string = "{} - {}".format \
                (tag_to_str(MPD_TAG_ARTIST), tag_to_str(MPD_TAG_TITLE)
                 )

            self.libmpdclient.mpd_song_free(song)

        volume_string = ""

        if -1 != volume:
            num_bars = 5
            num_full_bars = int(round(volume / (100. / num_bars)))

            volume_string = " {}{}".format \
                ("▮" * num_full_bars, "▯" * (num_bars - num_full_bars)
                 )

        return "{} {}{}".format \
            (state_string, song_string, volume_string
             )


if __name__ == '__main__':
    m = Mpd()
    print m.status().encode('utf-8')
