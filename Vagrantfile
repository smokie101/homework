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

  config.vm.define "worker" do |worker|
    worker.vm.box = "centos/7"
    worker.vm.hostname = "worker"
    worker.vm.network :private_network, ip: "192.168.55.254"

    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/worker.yml"
      ansible.become = true
      ansible.groups = { 'worker' => ['worker'] }
    end

  end

end