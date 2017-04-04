# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision :shell, path: "bootstrap.sh"
  config.vm.provision :hostmanager

  config.vm.network "private_network", type: "dhcp"
  config.vm.hostname = "my-hadoop"

  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "4096"
    vb.cpus = 2
  end
end
