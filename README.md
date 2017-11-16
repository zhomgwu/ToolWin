这几天花了点时间学习python，最后发现了几个python的UI引擎：
1. Tkinter；
2. wxPython；
3. wxQt；

于是顺便学了下wxPython，方便以后写一些工具来辅助项目开发，比如一些配表工具，一些代码生成工具等等。学习了2天之后，照着自己想的写了基础的模板，以后在这基础上添加功能即可，遂创建项目记录一下。

代码使用wxPython，基于python2.7，需要：
1. wx module；
2. py2exe；

wxmodule是wxPython基础库，使用 pip可以安装，命令为： pip install -U wxPython
py2exe是基于Distutils的工具，用来打包成exe，这样在其它机器上就不用安装python，安装包放在soft-package里。安装包其实也是库，安装的时候会安装到python/Lib/site-package，site-package是sys.path里的其中一个搜索路径，所以安装时稍稍注意下，安装包自己会找到本地的python路径并正确安装。

生成exe
在setup.py中配置好launcher，使用命令python setup.py py2exe 即可在dist中生成对应的exe文件。
