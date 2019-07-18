安装输入法 
https://blog.csdn.net/yangziluomu/article/details/70138741
注意可能会安装失败 再执行一次 sudo apt-get -f install即可

安装chrome
https://blog.csdn.net/m0_37676373/article/details/78616715

git
https://blog.csdn.net/u010107350/article/details/75224690

vim
https://blog.csdn.net/qq_29961771/article/details/53018869




ubuntu14.04如何卸载mysql

第一步：
sudo rm /var/lib/mysql/ -R
删除mysql的数据文件
第二步：
sudo rm /etc/mysql/ -R
删除mqsql的配置文件
第三步：
sudo apt-get autoremove mysql* --purge
sudo apt-get remove apparmor
自动卸载mysql的程序
