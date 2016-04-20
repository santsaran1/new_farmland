# Farmland Security Design flow #

System boots 
There are 6 [PIR Motion sensors](http://www.instructables.com/id/PIR-Motion-Sensor-Tutorial/), used to monitor any kind of introdures.
All 6 sensors are mounted one above the other so that any height of animal(big or small) and human being are detected.
Create python thread which shall run in continuous while loop to read temperature/humidity and display same on LCD screen (16x2 Lines).
Refer the link [lcd-module-control-using-python](http://www.raspberrypi-spy.co.uk/2012/07/16x2-lcd-module-control-using-python/)
System will keep checking for any of these sensors go high in continuous while loop.
This infinite loop will break and comes out if any of sensors go high.
Immediately system shall capture the image through USB cam attached and will store in "~/farmaland_security/pics/" folder. 
The above file shall be named as with time and date, for ex: "DDMMYYY:HH:MM.jpg".
The above file shall be uploaded to cloud (dropbox). Kindly refer [How to use Dropbox cloud with Raspberrypi](http://raspi.tv/2013/how-to-use-dropbox-with-raspberry-pi)
Create a thread which shall start recording through USB cam for specified amount of time and saved under "~/farmaland_security/videos/" folder.
File is again named as with time and date for ex: "DDMMYYY:HH:MM.mp4", and uploaded to cloud.* * 

```
filename = '/path/to/output/myfile-%s.txt'%datetime.now().strftime('%Y-%m-%d_%H-%M')


```