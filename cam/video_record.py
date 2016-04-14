avconv -loglevel quiet -f video4linux2 -r 10  -t 00:00:40 -i /dev/video0 test.avi
fswebcam -r 640x480 --jpeg 85 -D 1 shot.jpg
