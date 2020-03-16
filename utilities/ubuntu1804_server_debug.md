# Ubuntu 18.04 server debug

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
