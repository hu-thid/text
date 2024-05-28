import matplotlib.pyplot as plt
import numpy as np

class DataPlot:
	'''绘图
	'''
	def __init__(self,figureNum=1):
		self.figureNum = figureNum
		self.subplotNum = 211
		self.isFirst_DrawOneGraph = 1
		self.color = ['b','g','r','c','m','y','k','tan']

	def DrawOneGraph(self,DataList_x,DataList_y,LabelList):  
		'''在一幅图中绘制,
		DataList_x: x轴数据列表
        DataList_y: y轴数据列表
		LabelList: 标签列表
		'''
		if self.isFirst_DrawOneGraph :
			self.isFirst_DrawOneGraph = 0
			self.DataListNum = len(DataList_y)
			self.DataList_x = np.zeros([self.DataListNum,2])
			self.DataList_y = np.zeros([self.DataListNum,2])
			plt.ion()
			plt.figure(self.figureNum)			
			plt.grid()
			for i in range(0,self.DataListNum):	
			    ##### 横坐标 #####
				self.DataList_x[i][0] = DataList_x[i]
				self.DataList_x[i][1] = DataList_x[i]                
			    ##### 纵坐标 #####
				self.DataList_y[i][0] = DataList_y[i]
				self.DataList_y[i][1] = DataList_y[i]
				plt.plot(self.DataList_x[i], self.DataList_y[i],linestyle='-',color=self.color[(i)%len(self.color)],label=LabelList[i])
				plt.legend(loc='upper right')
		for i in range(0,self.DataListNum):
            ##### 横坐标 #####
			self.DataList_x[i][0] = self.DataList_x[i][1]
			self.DataList_x[i][1] = DataList_x[i]
            ##### 纵坐标 #####
			self.DataList_y[i][0] = self.DataList_y[i][1]
			self.DataList_y[i][1] = DataList_y[i]
			plt.figure(self.figureNum)
			plt.plot(self.DataList_x[i], self.DataList_y[i],linestyle='-',color=self.color[(i)%len(self.color)])
			plt.pause(0.001)

	def DrawMultipleGraphs(self,DataList_x,DataList_y,LabelList):
		print(1)



if __name__ == '__main__':

    Graph = DataPlot(0)
    for i in np.arange(0, 10):
        y1 = i
        y2 = 2*i

        xList = [ i, i ]
        yList = [ y1, y2 ]
        labelList = ['y1','y2']
        Graph.DrawOneGraph( xList, yList, labelList)



