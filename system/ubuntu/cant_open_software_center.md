ubuntu14.04无法打开软件中心的问题  
==

1. 确保`/user/bin/python`指向的是**python2.7**

2. `sudo apt-get update`

3. `sudo apt-get autoremove --purge software-center`

4. `sudo apt-get install -f software-center`
