# Ubuntu14.04 安装 gitlab

### 安装vim

```python
# Install vim and set as default editor
sudo apt-get install -y vim
sudo update-alternatives --set editor /usr/bin/vim.basic
```



###安装git(源码编译)

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

