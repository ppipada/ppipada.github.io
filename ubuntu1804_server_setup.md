# Ubuntu 18.04 server debug/setup

1. Disabling floppy drive: Error: `print_req_error: I/O error, dev fd0, sector 0`

   ```shell
   sudo rmmod floppy
   sudo echo "blacklist floppy" | sudo tee /etc/modprobe.d/blacklist-floppy.conf
   sudo dpkg-reconfigure initramfs-tools
   ```

2. Error: Network not up: eth/ens doesnt show or no service network-manager

   ```shell
   sudo dhclient
   sudo apt update
   sudo apt install network-manager ifupdown
   sudo service network-manager restart
   sudo systemctl status NetworkManager.service

   sudo vi /etc/netplan/01-netcfg.yaml
        # This file describes the network interfaces available on your system
        # For more information, see netplan(5).
        network:
        version: 2
        renderer: NetworkManager
        ethernets:
            ens32:
            dhcp4: yes
   sudo netplan generate
   sudo netplan apply
   ```

3. ssh setup

   ```shell
   ## For regenerating only rsa key
   sudo ssh-keygen -t rsa -b 4096 -f ssh_host_rsa_key
   ## For regenerating all missing keys
   sudo ssh-keygen
   # service ssh restart
   sudo systemctl status ssh
   ```

4. Fix non-configured locales

   ```shell
   sudo locale-gen en_US en_US.UTF-8
   sudo dpkg-reconfigure locales
   ```

5. Create a ntfs partition from an empty disk

   ```shell
   sudo fdisk /dev/sdb
   # fdisk is interactive
   # press m for help
   # Press p to list any available partitions
   # create a new partition by using n
   # after altering partitions press w to write
   # make a ntfs file system with "quick format" i.e dont write zeroes and dont check for bad sectors
   # remove f for full format
   mkfs.ntfs -f /dev/sdb1
   blkid
   # Note the UUID of the partition E.g: /dev/sdb1 UUID="asdfg1246"
   # Adding a entry in /etc/fstab
        UUID=asdfg1246   /disk1 ntfs-3g    permissions,locale=en_US.utf8    0   2
   ```

6. Samba setup

   ```shell
   sudo apt update
   sudo apt install samba
   # Allow Samba in ufw firewall
   sudo ufw allow 'Samba'
   sudo systemctl status smbd
   # Create a directory to host Samba share
   sudo mkdir /disk1/samba

   #### User setup
   sudo useradd -M -d /disk1/samba/peewee -s /usr/sbin/nologin -G sambashare peewee
   sudo mkdir /disk1/samba/peewee
   sudo chown peewee:sambashare /disk1/samba/peewee
   sudo chmod 2770 /disk1/samba/peewee
   sudo smbpasswd -a peewee # set password here
   sudo smbpasswd -e peewee
   vi /etc/samba/smb.conf

     [peewee]
        path = /disk1/samba/peewee
        browseable = yes
        read only = no
        force create mode = 0660
        force directory mode = 2770
        valid users = peewee

   sudo systemctl restart smbd
   sudo systemctl restart nmbd
   ```
