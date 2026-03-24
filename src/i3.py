__prefs__ = ('720', '360', 'webm')
__amftpl__ = ('\0\x03\0\0\0\x01\0!player.playerHandler.getVideoData\0\x02/1'
              '\0\0\0!\n\0\0\0\x04\x02\0\n{vid}\0@(\0\0\0\0\0\0\x02\0\0\x02\0\0')

from urllib.request import urlopen

def main():
    url = 'https://embed.indavideo.hu/player/video/2e844479a2'
    url2 = '2e844479a2'
    amfreq = __amftpl__.format(vid=url2).encode('utf-8')  # Convert to bytes!
    aa = urlopen('http://amfphp.indavideo.hu/gateway.php', data=amfreq).read()
    print(aa.decode('utf-8', errors='ignore'))  # Decode response for readability

if __name__ == "__main__":
    main()
