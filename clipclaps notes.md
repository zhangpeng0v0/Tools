# My Google:

> > ```账号：deerking321@gmail.com```
> >
> > ```密码：zp920316```

# news API

> >```markdown
> >deerking007   16601348816@163.com  
> >BBC  api_key='cb7a4ae15a98429890aeedb9a7b460a0'
> >
> >zhangpeng     zhangpeng@clipclaps.com
> >ABC    e7d5104fc5c74e259dbe2427b68257fb
> >```


> >
> > 查看ssh历史
> >
> > history | grep ssh
> >
> > ####登陆跳板机：
> >
> > ssh -i usEast01-sshkey-devuser.pem devuser@<54.204.52.128>
> >

> > 上传文件先由本地上传到跳板机
> >
> > scp -i usEast01-sshkey-devuser.pem /Users/zp/Desktop/news/saveSqldb.py devuser@54.204.52.128:/home/devuser
> >
> > 上传到服务器
> >
> > scp topbuzz.py devuser@10.1.15.11:/app/crawler/project/news
> >
> > 执行python环境
> >
> > ####启用python3.7环境执行命令 **
> >
> > . pyth3 或 source pyth3
> >
> > export PYTHONPATH=~/.local/lib/python3.7/site-packages
> >
> > virtualenv .
> >
> > 取消python3.7环境执行命令
> >
> > nopyth3
> >
> > telnet localhost 30008
> >
> > telnet 127.0.0.1 30008
> >


> > ```正则匹配键值对:"\"param\":\\{([^\\}]*)\\}"```



# 修改Terminal  >  fish

> > ``` you can use `chsh` to set default shell to `/usr/local/bin/fish```

> > 进入Terminal直接是fish界面

> > **```配置环境: vi ~/.config/fish/config.fish```**

> > ```vi ~/.bash_profile```

# Terminal工具

> >> **tig让git命令行可视化**
> >>
> >> ```brew install tig tree ag fzf```
> >
> >> **工具**
> >>
> >> ```brew install neovim```
> >
> >> **Terminal工具**
> >>
> >> `brew install tmux`
> >
> >> `brew install coreutils reattach-to-user-namespace axel git-extras fswatch mmv expect yarn`
> >
> >> ```sudo 超级用户```
> >
> >> ls -l 查看权限
> >>
> >> 赋值权限 sudo chown -R mr.zhang:staff wpsoffice.app/

# python3安装与卸载

## 安装

```markdown
>>> mac Terminal    brew install python
```

## 卸载

```markdown
>>> mac Terminal   
1.删除Python 3.X frameworksudo 
rm -rf /Library/Frameworks/Python.framework/Versions/3.6
2.删除Python 3.6 应用目录
sudo rm -rf “/Applications/Python 3.6”
3.删除/usr/local/bin 目录下指向的Python3.6的连接
cd /usr/local/bin/ 
ls -l /usr/local/bin | grep ‘/Library/Frameworks/Python.framework/Versions/3.6’  brew prune 
4.Python3.6的信息配置在 ~/.bash_profile 文件中，将其相关信息删除

```
