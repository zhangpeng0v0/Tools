# Ubuntu14.04 安装 gitlab

### 安装vim

```python
# Install vim and set as default editor
sudo apt-get install -y vim
sudo update-alternatives --set editor /usr/bin/vim.basic
```

### 安装git(源码编译)

```python
# Install dependencies
sudo apt-get install -y libcurl4-openssl-dev libexpat1-dev gettext libz-dev libssl-dev build-essential

# Download and compile pcre2 from source
curl --silent --show-error --location https://ftp.pcre.org/pub/pcre/pcre2-10.33.tar.gz --output pcre2.tar.gz
tar -xzf pcre2.tar.gz
cd pcre2-10.33
chmod +x configure
./configure --prefix=/usr --enable-jit
make
sudo make install

# Download and compile from source
cd /tmp
curl --remote-name --location --progress https://www.kernel.org/pub/software/scm/git/git-2.21.0.tar.gz
echo '85eca51c7404da75e353eba587f87fea9481ba41e162206a6f70ad8118147bee  git-2.21.0.tar.gz' | shasum -a256 -c - && tar -xzf git-2.21.0.tar.gz
cd git-2.21.0/
./configure --with-libpcre
make prefix=/usr/local all

# Install into /usr/local/bin
sudo make prefix=/usr/local install

# When editing config/gitlab.yml (Step 5), change the git -> bin_path to /usr/local/bin/git
```

### 安装邮件服务器

```python
# 安装(安装Postfix期间选择 'Internet Site' )
sudo yum install curl openssh-server openssh-clients postfix cronie
sudo service postfix start
sudo chkconfig postfix on
#这句是用来做防火墙的，避免用户通过ssh方式和http来访问。
sudo lokkit -s http -s ssh

    
# 卸载
apt-get purge postfix
```

### 添加并安装GitLab包

```python
curl -LJO http://mirror.tuna.tsinghua.edu.cn/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce-XXX.deb
#（在浏览器中输入http://mirror.tuna.tsinghua.edu.cn/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce就能看到要选择的gitlab版本软件 XXX表示版本号，我用的是gitlab-ce_7.14.3-ce.1_amd64.deb）

dpkg -i gitlab-ce-XXX.deb                         
#在安装的过程中会有一个让其输入主机名称，这时候如果不想设置名称，可以直接设置为IP地址，以方便登录
#如果设置为了主机名称，在自己本机（hosts）中或者DNS中要添加对服务器名称的dns解析。

#上面的那个命令安装完成后会显示如下的提示：
gitlab: GitLab should be reachable at http://ubuntu   #这个http://ubuntu就是待会要登录的gitlab主页，所以需要将其主机的解析加入到hosts文件中，
#如果上面命令中填的是IP,则不用添加到hosts中
gitlab: Otherwise configure GitLab for your system by editing /etc/gitlab/gitlab.rb file
gitlab: And running reconfigure again.
gitlab: 
gitlab: For a comprehensive list of configuration options please see the Omnibus GitLab 

readme
gitlab: https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/README.md
gitlab: 
It looks like GitLab has not been configured yet; skipping the upgrade script.
```

### 配置和使用GitLab

```python
sudo gitlab-ctl reconfigure
```

### 在浏览器访问GitLab主机名

```python
# 如果安装gitlab的linux主机IP是192.168.0.10或者ubuntu(ubuntu为gitlab服务器的名字)，就在浏览器中输入192.168.0.10或者http://ubuntu，刷新一次，会让输入新的root密码。登录成功。
```

