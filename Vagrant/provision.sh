#!/bin/bash

sudo apt update -y

sudo apt upgrade -y

sudo apt install software-properties-common

sudo apt-add-repository ppa:ansible/ansible

sudo apt install ansible -y

sudo echo "[deploy]" >> /etc/ansible/hosts

sudo echo "192.168.33.11 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant" >> /etc/ansible/hosts

# sudo echo "[app]" >> /etc/ansible/hosts

# sudo echo "192.168.33.12 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant" >> /etc/ansible/hosts

sudo apt-get install sshpass

export ANSIBLE_PASS=vagrant

sshpass -p "$ANSIBLE_PASS" ssh -o StrictHostKeyChecking=no vagrant@ansible

sudo rm /etc/ansible/ansible.cfg

sudo cp /home/ubuntu/ansible/ans.cfg /etc/ansible/ansible.cfg

ansible-playbook -v /home/ubuntu/ansible/playbook.yml
