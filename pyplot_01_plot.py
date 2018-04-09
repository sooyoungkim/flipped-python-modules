import numpy as np
import matplotlib.pyplot as plt

########################################################
# plot 그리기
# plot([y])에 a single list or array 를 주면
#   - y의 순차 값으로 가정하고 자동으로 x 값을 생성한다.
#   - 파이썬의 ranges()는 0부터 시작, y의 길이만큼 생성
# the x-axis ranges from 0-3
# the y-axis from 1-4
########################################################
plt.plot([1,2,3,4])        # y, b- (default) : a solid blue line
plt.ylabel('some numbers') # y축 라벨링
plt.show()


########################################################
# plot 그리기
# plot([x], [y], the optional format string
#                   - the color and line type)
########################################################
plt.plot([1,2,3,4], [1,4,9,16], 'ro') # x, y, red circles
plt.axis([0, 6, 0, 20]) # 축의 viewport [xmin, xmax, ymin, ymax]
plt.show()


########################################################
# 여러개의 plot 한번에 그리기
# plot([x1], [y1], the optional format string,
#      [x2], [y2], the optional format string,
#      [x3], [y3], the optional format string
#       등등.. )
#
########################################################
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
t
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


########################################################
# attributes 설정하는 방법들
# 방법 1. Use keyword args
# 방법 2. Use the setter methods of a Line2D instance
# 방법 3. Use the setp() command
#     3-1. use keyword args
#     3-2. or MATLAB style string value pairs
########################################################
x = [1,2,3,4]
y = [1,4,9,16]

# 방법 1. Use keyword args
plt.plot(x, y, linewidth=5.0)
plt.show()


# 방법 2. Use the setter methods of a Line2D instance
line, = plt.plot(x, y, '-')
line.set_linewidth(3.0)
line.set_color("orange")
line.set_antialiased(False) # turn off antialising
plt.show()


x1 = [1,2,3,4]
y1 = [1,4,9,16]
x2 = [3,5,7,9]
y2 = [6,2,3,6]

# use tuple unpacking
line1, line2 = plt.plot(x1, y1, x2, y2)

line1.set_linewidth(3.0)
line1.set_color("orange")
line1.set_antialiased(False)

line2.set_linewidth(1.0)
line2.set_color("black")
line2.set_antialiased(False)
line2.set_linestyle('-.')

plt.show()


# 방법 3. Use the setp() command
# 3-1. use keyword args
lines = plt.plot(x1, y1, x2, y2)
plt.setp(lines, color='g', linewidth=2.0)
plt.show()


# 3-2. or MATLAB style string value pairs
lines = plt.plot(x1, y1, x2, y2)
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
plt.show()
