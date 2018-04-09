########################################################
# Working with multiple Figures and Axes
#  한 화면에 여러 개의 그래프를 그리려면
#  figure 함수를 통해 Figure 객체를 먼저 만든 후
#  subplot 메서드를 통해 그리려는 그래프 개수만큼 subplot을 만들면
########################################################
import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)


# Figure 안에 subplot이 존재한다.
# figure(1) 디폴트로 생성된다. 사용여부는 옵션이다.
# subplot(numrows, numcols, fignum)
#   - fignum ranges from 1 to numrows * numcols
#   - The commas in the subplot command are optional if numrows * numcols < 10.
#       - 즉, subplot(211) 은 subplot(2, 1, 1)과 같다.
#
# (2, 1, 1)은  Figure 1 안에 2x1(행x열) 형상의 subplot을 생성한다는 의미이고
#   - 세 번째 인자 1은 생성된 2x1(행x열)의 subplot 중 첫 번째 subplot을 의미
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#   - 세 번째 인자 2는 생성된 2x1(행x열)의 subplot 중 두 번째 subplot을 의미
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')


# 다수의 Figures 사용가능하고, 여러개의 axes와 subplots을 포함할 수 있다.
plt.figure(2)
# (1, 2, 1)은  Figure 2 안에 1x2(행x열) 형상의 subplot을 생성한다는 의미이고
#   - 세 번째 인자 1은 생성된 1x2(행x열)의 subplot 중 첫 번째 subplot을 의미
plt.subplot(121)
plt.plot([1, 2, 3])
plt.title('Easy as 1, 2, 3')
#   - 세 번째 인자 2는 생성된 1x2(행x열)의 subplot 중 두 번째 subplot을 의미
plt.subplot(122)
x = range(0, 100)
y = [v*v for v in x]
plt.bar(x,y)


plt.figure(3)                # a third figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default


plt.show()
