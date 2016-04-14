from subprocess import call  
photofile = "/home/pi/dropbox/dropbox_uploader.sh upload /home/pi/cam/shot.jpg Servielence_videos/photo00001.jpg"   
call ([photofile], shell=True) 
