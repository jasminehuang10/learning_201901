import matplotlib.pyplot as plt

from learning.test_matplotlib import Randomwalk

#只要程序处于活动状态，就不断的模拟漫步
while True:
    # 创建一个Randomwalk实例，并将其包含的点都绘制出来
    rw = Randomwalk(500)
    rw.fill_walk()
    #第一种
    #plt.scatter(rw.x_value, rw.y_value, s=15)
    #第二种
    #point_numbers=list(range(rw.num_points))
    #plt.scatter(rw.x_value,rw.y_value,c=point_numbers,cmap=plt.cm.Blues,
    #            edgecolors="none",s=15)
    #分子运动
    plt.plot(rw.x_value,rw.y_value,linewidth=4)

    #突出起点和终点
    plt.scatter(0,0,c="green",edgecolors="none",s=100)
    plt.scatter(rw.x_value[-1],rw.y_value[-1], c="red", edgecolors="none",
                s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running=input("Make another walk?(y/n):")
    if keep_running == "n":
        break