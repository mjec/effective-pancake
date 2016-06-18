# -*- mode: ruby -*-
# vi: set ft=ruby :

# YOU NEED TO MAKE CHANGES TO THIS FILE! THERE IS POTENTIALLY
# MALICIOUS CODE IN HERE!
#  __          __       _____   _   _  _____  _   _   _____ 
#  \ \        / //\    |  __ \ | \ | ||_   _|| \ | | / ____|
#   \ \  /\  / //  \   | |__) ||  \| |  | |  |  \| || |  __ 
#    \ \/  \/ // /\ \  |  _  / | . ` |  | |  | . ` || | |_ |
#     \  /\  // ____ \ | | \ \ | |\  | _| |_ | |\  || |__| |
#      \/  \//_/    \_\|_|  \_\|_| \_||_____||_| \_| \_____|
#
# YOU NEED TO MAKE CHANGES TO THIS FILE! THERE IS POTENTIALLY
# MALICIOUS CODE IN HERE!
#
# Lesson one is to make sure you don't just run arbitrary
# code because I told you to. In particular:
#
#  * line 35 currently forwards your /etc folder to the
#    Vagrant box. This is a bad thing. I mean, it is disabled
#    because I'm nice but you should comment out this line.
#
#  * lines 45-52 currently run provision_insecure.py which
#    prints a scary warning telling you to edit this file.
#    Delete these lines to suppress that warning.




Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 80, host: 8080

  config.vm.synced_folder ".", "/vagrant"
  config.vm.synced_folder "/etc", "/host_etc", disabled: true

  config.vm.provision "shell",
    privileged: true,
    keep_color: false,
    name: "provision",
    inline: <<-SHELL
    /vagrant/setup/provision.sh
  SHELL

  config.vm.provision "shell",
    privileged: false,
    keep_color: true,
    name: "insecure",
    run: "always",
    inline: <<-SHELL
    /vagrant/setup/provision_insecure.py
  SHELL
end
