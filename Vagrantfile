# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
APT_OPTS="-uy -q --force-yes --allow-unauthenticated --no-install-recommends"
apt-get update $APT_OPTS
apt-get install gcc python-dev $APT_OPTS
apt-get install python-pip $APT_OPTS
sudo pip install -r /vagrant/requirements.txt
sudo pip install django-debug-toolbar
SCRIPT


# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "opscode-debian-8.5"
  config.vm.box_url = "http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_debian-8.5_chef-provisionerless.box"

  config.vm.synced_folder ".", "/vagrant", type: "rsync", rsync_exclude: ".git"

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 1
  end

  config.vm.provision "shell", inline: $script

  config.vm.network :private_network, ip: "192.168.35.11"


end
