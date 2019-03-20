# face_Face-recognition_openCV
face_Face recognition+openCV
Face_ recognition的安装配置
Window下通过Anaconda安装
 
注意python版本一定选择3.6 ！！！
点击Create，然后等待一段时间虚拟环境创建完毕
再打开 
通过指令 activate face_python进入到刚刚创建的虚拟环境
 

通过指令conda list看一下pip版本
 

由于安装Dlib库需要的最低pip版本需要>10
所以该Pip版本过低，先升级一下pip
python -m pip install --upgrade pip
 
然后pip install dlib安装Dlib库
这里Dlib一定要安装19.7.0以上的版本，不然会有很多麻烦
如果电脑上没有配置好boost和cmake会报错
在这里我就直接把我编译好的Dlib.whl文件上传百度网盘了，自己编译报错的话可以直接下载，下载完可以直接pip install 安装
（百度搜索pip安装whl文件，超简单）

安装好Dlib之后
通过指令：pip install face_recognition 安装face_recognition
 

接下来安装opencv 
直接指令：pip install opencv_python就OK啦
Pycharm配置方法：
打开pycharm
然后new一个Project
 
在数据集文件里放入训练的照片，修改代码里读取照片的路径
就可以运行了。
 


 







