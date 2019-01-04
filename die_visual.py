from learning.test_pygal import Die
import pygal

#创建一个D6
die=Die()

#投几次骰子，并将结果储存在一个列表中
'''results=[]
for roll_num in range(1,100):
    result=die.roll()
    results.append(result)'''
#上边的for循环改成解析列表
results=[die.roll() for roll_num in range(1,100)]

#分析结果
'''frequencies=[]
for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)'''
#上边的for循环改成解析列表
frequencies=[results.count(value) for value in range(1,die.num_sides+1)]

#对结果进行可视化

hist=pygal.Bar()

hist.title="Result of rolling one D6 1000 times"
hist.x_labs=[i for i in range(1,7)]
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add("D6",frequencies)
hist.render_to_file("die_visual.svg")