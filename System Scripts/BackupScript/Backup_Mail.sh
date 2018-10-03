#!/bin/bash
# Script for backup with e-mail confirmation.
# Author: Marta Laís, 2018. https://github.com/martalais/

# Identify your HD for backup and replace with "/dev/sdc*".
# "/mnt/BACKUP" is the dir where your HD will be mounted.
mount /dev/sdc* /mnt/BACKUP


# "mounted" check if the HD was mounted correctly.
# Replace "/sdc*" with the path of your backup HD.
mounted=`mount | grep /mnt/sdc*`

# Replace with your email adress.
EMAIL=`your@email.com`

if [ -z "$mounted" ]; then

	echo "ERROR: Unable to mount."
	sendemail -f "$EMAIL" -t "$EMAIL" -u "Backup." -m "Backup failed!" -s smtp.gmail.com:587 -xu "$EMAIL" -xp <passwd>
	exit 1

else
	echo "Mounted!"
	DATA=`date +%Y-%m-%d-%H.%M`
	
	cd /mnt/BACKUP

	# Replace "/vbox" with the dir that you wish to backup.
	tar -zcvf BACKUP_"$DATA".tar.gz /vbox/.../
	umount /mnt/sdc*

	# Replace <PASSWORD> with your password adress.
	sendemail -f "$EMAIL" -t "$EMAIL" -u "Backup." -m "
Backup made successfully!" -s smtp.gmail.com:587 -xu "$EMAIL" -xp <PASSWORD>
fi
