from subprocess import call  
photofile = "/home/pi/farmland_security/dropbox/dropbox_uploader.sh upload /home/pi/farmland_security/cam/test.avi servielence_videos/test1.avi"   
call ([photofile], shell=True) 
