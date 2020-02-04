# coding=utf-8
import os
import ConfigParser

cf = ConfigParser.ConfigParser()

#基础设置
deep =10 #探索的深度
filename_filter=[]
def getallfile(path,f,level,high):
	high=high-1
	if high<0:
		return
	allfilelist=os.listdir(path)

	filelist=[]
	dirlist=[]
	pathlist=[]
	len_dirlist=0
	# 遍历该文件夹下的所有目录或者文件
	for file in allfilelist:
		filepath=os.path.join(path,file)
		if os.path.isdir(filepath):
			if file in filename_filter:
				continue
			len_dirlist=len_dirlist+1
			dirlist.append(level+file+'\n')
			pathlist.append(filepath)
		else:
			if(os.path.splitext(file)[-1]!=''):
				filelist.append(file+" : \n")
	for filename in filelist:
		f.write(filename.encode('utf-8'))
	for i in range(len_dirlist):
		f.write(dirlist[i].encode('utf-8'))
		f.write('`文件夹说明` : \n')
		getallfile(pathlist[i],f,level+"#",high)

if __name__ == "__main__":
	# java工程分析
 	root_path=os.path.dirname(os.path.abspath(__file__))   # 表示当前所处的文件夹的绝对路径
 	# 读取配置属性
 	cf.read(root_path+'/config.conf')
 	rootdir=cf.get("base","rootdir").decode('utf-8')
 	resultdir=cf.get("base","result")
 	deep=cf.getint("base","deep")
 	filename_filter=cf.get("base","filter").split(',')
 	first_level=cf.getint("base","first_level")

 	# 开始工作
 	f=open(root_path+resultdir, 'a')
 	f.seek(0)
 	f.truncate()   #清空文件
 	getallfile(rootdir,f,first_level*'#',deep)
 	f.close()