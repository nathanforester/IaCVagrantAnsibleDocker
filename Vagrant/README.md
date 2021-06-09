# Local Deployment Example

## Using Vagrant as Local IaC

### Advantages:

- Good learning tool to see how nodes with hypervisors work
- Negates the security risks to your data compared to cloud based computing
- Gives a good insight into using virtual machines and networks

### Disadvatages:

- Deploying an entire project could be unnecessarily complex and time consuming
- For full business effectiveness, migration to cloud is still necessary

The first part of this project has been successfully completed. Vagrant configures two virtual machines using the VirtualBox plugin: one for containerisation and one for configuration. It is now ready for part two: continuous integration and deployment.

Updated: part two is now begun and development/feature branches have been implemented as good DevOps practices.

Updated further: The app has been fully deployed on an automated process from Vagrant ---> Ansible ----> Docker & Docker Compose ----> port 5000. Recommend putting the nginx process in the playbook.yml before the app deployment (may not be 100% effective) OR somehow introducing a systemd process, creating another AMI or image of that and then running it on an entirely separate node and/or container. The app itself now has full functionality on port 5000 and its CRUD API facility is fully functional.

if a test of the code is required, simply take the code and run "vagrant up" on an appropriate terminal (Windows Powershell, Gitbash, Linux etc). 
