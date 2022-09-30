# Python Project

## PyQt5 Project
### 配置
1. pycharm中安装pyqt5-tools依赖包（依赖包目前只支持到python3.9，最好安装python3.8版本）

2. 安装过后在**C:\Users\PaleRabbit\AppData\Local\Programs\Python\Python38\Lib\site-packages\qt5_applications\Qt\bin\designer.exe**路径中找到designer运行文件

3. ui文件转py文件：

   添加外部工具

   `PyCharm` -> 文件 -> 设置 -> 工具 -> 外部工具

   先添加 `QT Designer` ，可以参考截图设置。

   - "名称" : 这里可以自定义的
   - "程序"：选择的是 "designer.exe" 的安装目录
   - "工作目录": 根据实际情况配置，这里我直接使用的是 宏 `$FileDir$`
   
   添加 `Pyuic`

   - "名称": 这里可以自定义的
   - "程序"：选择的是 "pyuic5.exe" 的安装目录
   - "实参"：`$FileName$ -o $FileNameWithoutExtension$.py`
   - 意思将选中的 `xxx.ui` 文件转换为同名的 `xxx.py`文件
   - 需要特别注意的是，执行的时候需要右键选中对应的 `xxx.ui` 文件，不然会出错的。
   - "工作目录": 根据实际情况配置，这里我直接使用的是 宏 $FileDir$

### 打包配置

添加 `Pyinstaller`

- "名称": 这里可以自定义的
- "程序"：选择的是 "pyinstaller.exe" 的安装目录
- "实参"：`-F $FileNameWithoutExtension$.py`
  -  -F 表示生成单个可执行文件
  -  -w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！
  -  -p 表示你自己自定义需要加载的库路径
  -  -i 表示可执行文件的图标(如果你想自定义图标则添加此项并在后面添加ico文件目录)
- "工作目录": 根据实际情况配置，这里我直接使用的是 宏 $FileDir$

打包文件会生成spec文件，build文件夹和dist文件夹

**spec文件**：pyinstaller首先会生成spec格式的文件，这个你在打包目录下直接可以找到，而pyinstaller是直接根据这个文件的内容来打包的，事实上你可以用文本编辑软件比如sublime text打开，会看到其中使用Python语法的内容，内容包含了所有打包的信息，其中有一个比较重要的是，spec文件里有个pathex列表变量，里面存储了一些打包时要用到的库所在的路径（不一定全部，所以可能在打包时出现找不到库的问题）。所以我建议pyinstaller使用spec文件打包，而不是直接使用命令打包。

**build文件夹**：，里面存储了打包过程中出现的各种问题和信息，包括日志文件等，可以找到日志文件查看打包过程中出现的问题。

**dist文件夹**：那就是放exe文件的地方


## Office Project

