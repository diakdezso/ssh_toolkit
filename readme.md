<b>Aim : An SSH Toolkit for adding/removing public keys on multiple instances through SSH developed by Diák Dezső</b>


setup:

1.) First make sure you have all the files you need in the same directory:
- connector.py
- ssh-pro-config.py
- ssh-toolkit_pro.py

2.) Now you can generate your json config files with ssh-pro-config.py

3.) Enjoy!:)

usage: ssh-toolkit_pro.py [-h] [-list] [-add] [-remove]

optional arguments:
  -h, --help  show this help message and exit
  -list       Lists out the authorized_keys by hosts on multiple remote hosts to console
  -add        Add public key to authorized_keys on multiple remote hosts
  -remove     Remove public key from authorized_keys on multiple remote hosts

