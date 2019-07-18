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




一、删除php的相关包及配置
sudo apt-get autoremove php7*

二、删除关联
sudo find /etc -name "*php*" |xargs  rm -rf 

三、清除dept列表
sudo apt purge `dpkg -l | grep php| awk '{print $2}' |tr "\n" " "`

四、检查是否卸载干净（无返回就是卸载完成）
 dpkg -l | grep php7.0



1.安装apache2

安装命令：sudo apt-get install apache2

启动/停止/重启apache2: service apache2 start/stop/restart



2. 卸载apache2

之前卸载重新安装后找不到apache2.conf配置文件，测试使用一下方式卸载后可用。

(1)  $ sudo apt-get --purge remove apache2
       $ sudo apt-get --purge remove apache2.2-common
       $ sudo apt-get autoremove

(2) （关键一步）找到没有删除掉的配置文件，一并删除
       $ sudo find  /etc -name "*apache*" -exec  rm -rf {} \;
       $ sudo rm -rf /var/www
