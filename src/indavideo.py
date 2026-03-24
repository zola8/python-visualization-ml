# https://gist.github.com/mrtee/1394870#file-ivd-py

#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Downloader for http://indavideo.hu/
Author: András Veres-Szentkirályi <vsza@vsza.hu>
License: MIT
"""

from lxml import html
from urllib2 import urlopen
from subprocess import call
import re
import sys

__prefs__ = ('720', '360', 'webm')
__amftpl__ = ('\0\x03\0\0\0\x01\0!player.playerHandler.getVideoData\0\x02/1'
        '\0\0\0!\n\0\0\0\x04\x02\0\n{vid}\0@(\0\0\0\0\0\0\x02\0\0\x02\0\0')

def main():
    """Downloads the video from the URL in argv[1] (if specified)"""
    if len(sys.argv) < 2:
        print >> sys.stderr, 'Usage: %s <url>' % sys.argv[0]
    else:
        download(sys.argv[1])

def download(url):
    """Downloads the video from the URL in the url parameter"""
    videos = getvideos(url)
    video_url = preferred(videos)
    call(['wget', video_url])

def preferred(videos):
    """Returns the preferred URL from the iterable in the videos parameter"""
    for pref in __prefs__:
        for video in videos:
            if pref in video:
                return video
    return list(videos)[0]

def url2vid(url):
    """Returns the ID of the video on the URL in the url parameter"""
    video = html.parse(urlopen(url)).getroot()
    video_src = video.xpath('/html/head/link[@rel = "video_src"]/@href'
        ' | /html/head/meta[@property="og:video"]/@content')[0]
    return re.search('vID=([^&]+)&', video_src).group(1)

def getvideos(url):
    """Returns URLs that contain the video on the URL in the url parameter"""
    amfreq = __amftpl__.format(vid=url2vid(url))
    amfresp = urlopen('http://amfphp.indavideo.hu/gateway.php', amfreq).read()
    return set(re.findall(r'http://[a-zA-Z0-9/._]+\.(?:mp4|webm|flv)', amfresp))

if __name__ == "__main__":
    main()
