今天部署到server 中的代码倒包时出现问题，于是查了python 的import机制，以备忘： 

python中，每个py文件被称之为模块，每个具有__init__.py文件的目录被称为包。只要模块或者包所在的目录在sys.path中，就可以使用import 模块或import 包来使用。 

如果想使用非当前模块中的代码，需要使用Import，这个大家都知道。 
如果你要使用的模块（py文件）和当前模块在同一目录，只要import相应的文件名就好，比如在a.py中使用b.py： 
import b 
但是如果要import一个不同目录的文件(例如b.py)该怎么做呢？ 
首先需要使用sys.path.append方法将b.py所在目录加入到搜素目录中。然后进行import即可，例如 
import sys 
sys.path.append('c:\xxxx\b.py') # 这个例子针对 windows 用户来说的 
大多数情况，上面的代码工作的很好。但是如果你没有发现上面代码有什么问题的话，可要注意了，上面的代码有时会找不到模块或者包（ImportError: No module named xxxxxx），这是因为： 
sys模块是使用c语言编写的，因此字符串支持 '\n', '\r', '\t'等来表示特殊字符。所以上面代码最好写成： 
sys.path.append('c:\\xxx\\b.py') 
或者sys.path.append('c:/xxxx/b.py') 
这样可以避免因为错误的组成转义字符，而造成无效的搜索目录（sys.path）设置。 



但上述方法是针对脚本来说的，每次使用要记得加上，如果永久性的加入某个目录到sys.path中去呢？



**如何将路径“永久"添加到sys.path?**

sys.path是python的搜索模块的路径集，是一个list

可以在python 环境下使用sys.path.append(path)添加相关的路径，但在退出python环境后自己添加的路径就会自动消失了！

可以使用以下命令输入当前python 的搜索路径：

python -c"import sys;print '当前的python是:'+sys.prefix;print '\n'.join(sys.path)"

练习使用sys.path.append方法添加路径，显示退出python会消失！

python -c"import sys;print '当前的python是:'+sys.prefix;**sys.path.append(r'E:\DjangoWord')**;print '\n'.join(sys.path)"

再次运行，会发现 自己添加路径E:\DjangoWord()不存在了!

python -c"import sys;print '当前的python是:'+sys.prefix;print '\n'.join(sys.path)"

为解决这个问题，可以有以下方法：

![img](http://static.oschina.net/uploads/img/201302/21190348_xIRs.jpg)
将自己做的py文件放到 site_packages 目录下：

下面命令显示了 site-packages 目录：

python -c "**from distutils.sysconfig import get_python_lib; print get_python_lib()**"

 但是这样做会导致一个问题，即各类模块都放到此文件夹的话，会导致乱的问题，这一点是显而易见的。

 注意，也不创建子文件夹，再将自己的模块放到子文件夹解决问题，这会导致使用import 语句时错误。

![img](http://static.oschina.net/uploads/img/201302/21190348_UMEn.jpg)
使用pth文件，在 site-packages 文件中创建 .pth文件，将模块的路径写进去，一行一个路径，以下是一个示例，pth文件也可以使用注释：

\# .pth file for the  my project(这行是注释)
E:\DjangoWord
E:\DjangoWord\mysite
E:\DjangoWord\mysite\polls

这个不失为一个好的方法，但存在管理上的问题，而且不能在不同的python版本中共享。

![img](http://static.oschina.net/uploads/img/201302/21190348_JBZ7.jpg)
使用PYTHONPATH环境变量，在这个环境变量中输入相关的路径，不同的路径之间用逗号（英文的！)分开，如果PYTHONPATH 变量还不存在，可以创建它！如下图所示：

![img](http://static.oschina.net/uploads/img/201302/21190348_sytc.jpg)

这里的路径会自动加入到sys.path中，而且可以在不同的python版本中共享，应该是一样较为方便的方法。

关于与python相关的环境变量有那些，请参考：

[http://docs.python.org/using/cmdline.html](http://docs.python.org/using/cmdline.html)  在页面上找到PYTHONPATH

![img](http://static.oschina.net/uploads/img/201302/21190348_V7B3.jpg)
以下是该环境变量的描述：

PYTHONPATH[¶](http://docs.python.org/using/cmdline.html#envvar-PYTHONPATH)

Augment the default search path for module files. The format is the same asthe shell’s **PATH**: one or more directory pathnames separated by[os.pathsep](http://docs.python.org/library/os.html#os.pathsep) (e.g. colons on Unix or semicolons on Windows).Non-existent directories are silently ignored.

In addition to normal directories, individual [**PYTHONPATH**](http://docs.python.org/using/cmdline.html#envvar-PYTHONPATH) entriesmay refer to zipfiles containing pure Python modules (in either source orcompiled form). Extension modules cannot be imported from zipfiles.

The default search path is installation dependent, but generally begins withprefix/lib/pythonversion (see [**PYTHONHOME**](http://docs.python.org/using/cmdline.html#envvar-PYTHONHOME) above). Itis always appended to [**PYTHONPATH**](http://docs.python.org/using/cmdline.html#envvar-PYTHONPATH).

An additional directory will be inserted in the search path in front of[**PYTHONPATH**](http://docs.python.org/using/cmdline.html#envvar-PYTHONPATH) as described above under[Interface options](http://docs.python.org/using/cmdline.html#using-on-interface-options). The search path can be manipulated fromwithin a Python program as the variable [sys.path](http://docs.python.org/library/sys.html#sys.path).

附：python安装模块的多种方法

1、自己写的模块，可以直接添加到路径下。这样就可以直接调用。
import sys
sys.path.append("/home/username/")

2、单文件模块
直接把文件拷贝到$python_dir/lib

3、网上下载的第三方库，一般解压后，找setup.py文件
   运行python setup.py install

4、 egg文件
   1) 下载ez_setup.py,运行python ez_setup
   2) easy_install *.egg

5、pip安装方法
   Pip 是安装python包的工具，提供了安装包，列出已经安装的包，升级包以及卸载包的功能。
   Pip 是对easy_install的取代，提供了和easy_install相同的查找包的功能，因此可以使用easy_install安装的包也同样可以使用pip进行安装。
   安装Pip
   Pip的安装可以通过源代码包，easy_install或者脚本。
   下面介绍一下各种安装方法：
   源代码方式：
   $ wget https://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz （替换为最新的包）
   $ tar xzf pip-1.2.1.tar.gz
   $ cd pip-1.2.1.tar.gz
   $ python setup.py install
   easy_install:
   $ easy_install pip
   get_pip.py 脚本：
   $ curl -0 https://raw.github.com/pypa/pip/master/contrib/get-pip.py
   $ sudo python get-pip.py
   OK, 下面来看一下Pip的使用
   安装package
   $ pip install Markdown
   列出安装的packages
   $ pip freeze
   安装特定版本的package
   通过使用==, >=, <=, >, <来指定一个版本号。
   $ pip install 'Markdown<2.0'
   $ pip install 'Markdown>2.0,<2.0.3'
   升级包
   升级包到当前最新的版本，可以使用-U 或者 --upgrade
   $ pip install -U Markdown
   卸载包
   $ pip uninstall Markdown
   查询包
   pip search "Markdown"

6、特殊库的安装（一个科学计算库Enthought Python Distribution的安装） 
  Enthought Python Distribution在ubuntu下安装的测试，应一个网友的请求，问怎么安装这个库，从官方网站上下载了一个文件
epd_free-7.3-2-rh5-x86.sh，遮个文件是sh 格式的文件，用sudo bash epd_free-7.3-2-rh5-x86.sh 运行这个文件，出现很多权限的阅读，点回车，不要连续点
需要点一次看一下，最后出现一个同一不同一它的版权声明，输入"yes",再下来是让选择安装的目录，点回车，就安装在当前目录下。
这样就安装好了。
当前目录下输入
\>>> ipython --pylab
就出来
Python 2.7.3 (default, Apr 20 2012, 22:44:07)
Type "copyright", "credits" or "license" for more information.
IPython 0.12.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
Welcome to pylab, a matplotlib-based Python environment [backend: TkAgg].
For more information, type 'help(pylab)'.
再这样调用。
In [1]: from scipy import *
In [2]: a=zeros(1000)
In 3]: a[:100]=1
In [4: b=fft(a)
In [5]: plot(abs(b))