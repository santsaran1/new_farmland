# Farmland Security Design flow #

1. System boots 
2. There are 6 [PIR Motion sensors](http://www.instructables.com/id/PIR-Motion-Sensor-Tutorial/), used to monitor any kind of introdures.
3. All 6 sensors are mounted one above the other so that any height of animal(big or small) and human being are detected.
4. Create python thread which shall run in continuous while loop to read temperature/humidity and display same on LCD screen (16x2 Lines).
5. Refer the link [lcd-module-control-using-python](http://www.raspberrypi-spy.co.uk/2012/07/16x2-lcd-module-control-using-python/)
6. System will keep checking for any of the sensors go high in continuous while loop.
7. This infinite loop will break and comes out if any of sensors go high.
8. Immediately system shall capture the image through USB cam attached and will store in "~/farmaland_security/pics/" folder. 
9. The above file shall be named as with time and date, for ex: "DDMMYYY:HH:MM.jpg".
10. The above file shall be uploaded to cloud (dropbox). Kindly refer [How to use Dropbox cloud with Raspberrypi](http://raspi.tv/2013/how-to-use-dropbox-with-raspberry-pi)
11. Create a thread which shall start recording through USB cam for specified amount of time and saved under "~/farmaland_security/videos/" folder.
12. File is again named as with time and date for ex: "DDMMYYY:HH:MM.mp4", and uploaded to cloud.* * 

13. **Creating pic/video file name with date and time**
```
videoFile = '~/farmaland_security/videos/farmVideo-%s.mp4'%datetime.now().strftime('%Y-%m-%d_%H-%M')
picFile = '~/farmaland_security/pics/farmPic-%s.jpg'%datetime.now().strftime('%Y-%m-%d_%H-%M')

```
14. **video recording for 40 seconds**
```
avconv -loglevel quiet -f video4linux2 -r 10  -t 00:00:40 -i /dev/video0 videoFile

```
15. **Capturing pic**

```
fswebcam -r 640x480 --jpeg 85 -D 1 picFile

```

16. [Interfacing SIM900A](https://elementztechblog.wordpress.com/2014/08/18/interfacing-sim900a-gsm-modem-with-raspberrypi/)
Sample code : [Code]( https://github.com/elementzonline/RaspberryPi-Sample-Codes/tree/master/GSM_class)


