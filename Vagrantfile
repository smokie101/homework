Vagrant.configure("2") do |config|

  config.vm.define "kafka" do |kafka|
    kafka.vm.box = "centos/7"
    kafka.vm.hostname = "kafka"
    kafka.vm.network :private_network, ip: "192.168.55.253"

    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/kafka.yml"
      ansible.become = true
      ansible.groups = { 'kafka' => ['kafka'] }
    end

  end

end