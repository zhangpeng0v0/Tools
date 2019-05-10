#Git :

自报家门：

git config --global user.name “  ”

git config --global user.email “  ”

创建Git仓库：

git init ……..    (ls -ah查看隐藏文件)

git add …   添加到缓存区

git commit -m “修改说明”

git status   查看缓存区状态

git diff …. 查看修改情况

git log    搜索历史记录及版本号

git reset —hard 版本号

git reflog  查看历史命令

git checkout --…….   丢弃缓存区修改

git rm …..  删除

将删除的缓存区内容复原

git reset HEAD ….

git checkout --……

创建公私钥

ssh-keygen -t rsa -C “email”

关联远程仓库

git remote add origin ……(GitHub 上库的ssh)

git push -u origin master   第一次push需要加-u

git clone git@….克隆

git branch

git branch …创建分支

git checkout …切换分支

git merge …合并分支

git branch -d …删除分支

git pull 更新项目



.gitignore  配置忽略提交的文件



wip 分支一定要开始习惯用，大概操作：

git checkout -b wip-Txx

git push --set-upstream

正常编码，随时提交，推送

和主干同步

git fetch

git merge origin/master

提交回主干

git checkout master

git merge origin/master

git merge --squash wip-Txx

看一下自己的修改

git status

git diff --cached

(可以用图形化的工具，https://www.sourcetreeapp.com/）

提交，推送

注意当前所在的分支，避免误操作 (spacefish 配置好后能直接看到状态）