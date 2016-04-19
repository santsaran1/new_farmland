# Farmland Security Design flow #

1. System boots 
2. There are 6 [PIR Motion sensors](http://www.instructables.com/id/PIR-Motion-Sensor-Tutorial/), used to monitor any kind of introdures.
3. All 6 sensors are mounted one above the other so that any height of animal(big or small) and human being are detected.
4. System will keep checking for any of these sensors go high in continuous while loop.
5. This infinite loop will break and comes out if any of sensors go high.
6. Immediately system shall capture the image through USB cam attached and will store in "~/farmaland_security/pics/" folder. 
7. The above file shall be named as with time and date, for ex: "DDMMYYY:HH:MM.jpg".
8. The above file shall be uploaded to cloud (dropbox). Kindly refer [How to use Dropbox cloud with Raspberrypi](http://raspi.tv/2013/how-to-use-dropbox-with-raspberry-pi)
9. Create a thread which shall start recording through USB cam for specified amount of time and saved under "~/farmaland_security/videos/" folder.
10. File is again named as with time and date for ex: "DDMMYYY:HH:MM.jpg", and uploaded to cloud.

```
filename = '/path/to/output/myfile-%s.txt'%datetime.now().strftime('%Y-%m-%d_%H-%M')


```