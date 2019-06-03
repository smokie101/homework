Vagrant.configure("2") do |config|

  config.vm.define "monitoring" do |monitoring|
    monitoring.vm.box = "centos/7"
    monitoring.vm.hostname = "monitoring"
    monitoring.vm.network :private_network, ip: "192.168.55.252"

    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/monitoring.yml"
      ansible.become = true
      ansible.groups = { 'monitoring' => ['monitoring'] }
    end

  end

end