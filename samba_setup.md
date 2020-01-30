# Samba setup

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
    ## Add these to the globals section to avoid name mangling and using appropriate charset
    # [globals]
    mangled names = no
    dos charset = CP850
    unix charset = UTF-8
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
