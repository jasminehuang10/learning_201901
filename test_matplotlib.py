
'''import matplotlib.pyplot as plt
"""简单的折线图"""
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)

#设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",labelsize=14)

plt.show()


import matplotlib.pyplot as plt
"""使用scatter绘制散点图并设置其样式"""

x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
#plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolors="none",s=40)
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors="none",\
                                                                     s=40)

#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",which="major",labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

#plt.show()
plt.savefig("squares_plot.png",bbox_inches="tight")



#15-2彩色立方
import matplotlib.pyplot as plt
"""使用scatter绘制散点图并设置其样式"""
x_values=list(range(1,5001))
y_values=[value**3 for value in x_values]
plt.scatter(x_values,y_values,edgecolors="none",s=30,c=y_values,
            cmap=plt.cm.Blues)

#设置图标标题并给坐标轴加上标签
plt.title("5000**********",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Value of 3",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,5000,0,5000**3])

plt.savefig("squares3.png",bbox_inches="tight")


#随机漫步
from random import choice

class Randomwalk():
    """一个生成随机漫步数据的类"""

    def __init__(self,num_points=500):
        """初始化随机漫步的属性"""
        self.num_points=num_points

        #所有随机漫步都始于(0,0)
        self.x_value=[0]
        self.y_value=[0]

    def get_step(self):
        # 决定前进方向以及沿这个方向前进的距离
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance

        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_direction * y_distance

        return x_step, y_step


    def fill_walk(self):
        while len(self.x_value) < self.num_points:
            """计算随机漫步包含的所有点"""
            x_step = self.get_step()[0]
            y_step = self.get_step()[1]

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            self.x_value.append(next_x)
            self.y_value.append(next_y)'''











