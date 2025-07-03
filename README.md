# Search4text
快捷搜索文本 题库搜索 测验辅助

适用于题库的搜索，通过读取剪切板的内容在Tooltip中显示对应内容

环境为Python 3.8，导出的exe在windows 7也可以使用

## 使用教程

将文本库/题库文件sample.txt放到与程序同一目录下

使用时,选取并复制(推荐使用快捷键`Ctrl + C`)要搜索的文本/题目,即可自动在Tooltip中显示对应内.只有当剪切板内容更新时才会显示Tooltip

![文本库](https://github.com/CodeLeee/Search4text/blob/main/images/1.png?raw=true)
![Tooltip显示内容](https://github.com/CodeLeee/Search4text/blob/main/images/2.png?raw=true)

## 文本库/题库制作

题库为txt格式，每行为一道题，txt中用`Tab`在Tooltip显示中的换行功能（见上图）

也可以将Excel题库导出为txt，每行为文本的一个词条

### 将文本库集成到exe的方法

在pyinstaller中加入`--add-data "example.txt;."`(在py文件注释中有）打包成exe，即可将文本库打包到exe。此时exe中包含题库，无需将题库放到exe的目录下也可正常使用

## 下载

[控制台版本](https://github.com/CodeLeee/Search4text/releases/download/Search4text_console/Search4text_console.exe)

[Chrome伪装版](https://github.com/CodeLeee/Search4text/releases/download/Search4text_Google/Search4text_Google.exe) （伪装成Chrome图标）

![](https://github.com/CodeLeee/Search4text/blob/main/images/4.png?raw=true)

[后台版](https://github.com/CodeLeee/Search4text/releases/download/Search4text_Google/Search4text_Google.exe) （在后台运行而不打开程序窗口，关闭需要使用任务管理器将进程关闭）

![](https://github.com/CodeLeee/Search4text/blob/main/images/3.png?raw=true)
