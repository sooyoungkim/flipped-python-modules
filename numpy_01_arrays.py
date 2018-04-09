import numpy as np

########################################################
# Arrays
#   - Numpy의 중심 feature는 Array object class이다.
#   - Python의 List와 비슷하지만 Array의 모든 원소는 같은 타입이다.
#   - 대개 float이나 int 타입
#   - 엄청 큰 numeric 데이터를 매우 빠르고 효과적으로 계산.
#   - Arrays 는 multidimensional이라 할 수 있다.
#   -  Array생성 : numpy.array(the list, the type)
########################################################

########################################################
# a one-dimensional array
one = np.array([1, 4, 5, 8], float)
print(one)

print(type(one))

# Array 원소들에 List처럼 접근, 슬라이싱, 조작 가능
one[:2]
one[3]
one[0]
########################################################

########################################################
# a two-dimensional array
two = np.array([[1, 2, 3], [4, 5, 6]], float)
print(two)
two[0,0]
two[0,1]
two[0,2]
two[1,0]
two[1,1]
two[1,2]

two[1, :]
two[:, 2]
two[-1:, -2:]

print(two.shape)    # (행 size, 열 size) 튜플 반환 -> (2,3)
print(two.dtype)    # array에 저장된 value의 타입 반환
                    # float64 : 파이썬에서 float타입과 비슷
                    #           NumPy는 실수를 배정밀도(8byte,64비트)로 처리
len(two)    # 행의 길이

2 in two    # array 안에 value 2가 존재하는지?
0 in two
########################################################


########################################################
# a one-dimensional array -> a two-dimensional array
arr = np.array(range(10), float)
print(arr)
# [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9.]

arr = arr.reshape((5,2))  # 10개 데이터가 담긴 1차원 배열을 -> 2차원의 새로운 배열로 생성
print(arr)
#[[ 0.  1.]
# [ 2.  3.]
# [ 4.  5.]
# [ 6.  7.]
# [ 8.  9.]]

print(arr.shape)    # (5,2)
########################################################


########################################################
a = np.array([1, 2, 3], float)
b = a           # reference 참조
c = a.copy()    # 메모리에서 분리, 새로운 array 생성
a[0] = 0        # a와 a를 참조하는 b에 영향

print(a)        # [0.   2.   3.]
print(b)
print(c)


a.tolist()      # arrays 를 리스트로 [0.0   2.0   3.0]
list(a)         # arrays 를 리스트로 [0.0   2.0   3.0]


s = a.tostring()        #  a binary string (i.e., not in human-readable form)으로 컨버팅
print(s)
print(np.fromstring(s)) # 이 a binary string 으로 array 생성

a.fill(0)
print(a)
########################################################


########################################################
# Transposed
a = np.array(range(6), float).reshape((2,3))
print(a)
#[[ 0.  1.  2.]
# [ 3.  4.  5.]]

print(a.transpose())
#[[ 0.  3.]
# [ 1.  4.]
# [ 2.  5.]]

print(a)        # 변경 없음
########################################################


########################################################
# a two-dimensional array -> a one-dimensional array
a = np.array([[1,2,3], [4,5,6]], float)
print(a)
#[[ 1.  2.  3.]
# [ 4.  5.  6.]]

print(a.flatten())
#[ 1.  2.  3.  4.  5.  6.]

print(a)        # 변경 없음
########################################################


########################################################
# a one-dimensional array
# 2개 이상의 배열을 하나로 합칠 수 있다.
a = np.array([1,2], float)
b = np.array([3,4,5,6], float)
c = np.array([7,8,9], float)
print( np.concatenate((a,b,c)) )

# a two-dimensional array
# 2차원 이상 배열도 하나로 합칠 수 있다.
a = np.array([[1, 2], [3, 4]], float)
b = np.array([[5, 6], [7,8]], float)
print(np.concatenate((a,b)))    # axis=0과 같다
print(np.concatenate((a,b), axis=0))
#[[ 1.  2.]
# [ 3.  4.]
# [ 5.  6.]
# [ 7.  8.]]
print(np.concatenate((a,b), axis=1))
#[[ 1.  2.  5.  6.]
# [ 3.  4.  7.  8.]]
########################################################


########################################################
# ?????
# 배열의 차원 수를 증가시킬 수 있다.
# 벡터와 행렬의 적절한 차원의 array를 생성하기 편리하다
a = np.array([1, 2, 3], float)
print(a[:, np.newaxis])
#[[ 1.]
# [ 2.]
# [ 3.]]
print(a[:, np.newaxis].shape)   # 1차원 배열 -> 3차원 배열로 (3,1)

print(a[np.newaxis, :])
# [[ 1.  2.  3.]]
print(a[np.newaxis, :].shape)   # (1,3)
########################################################

########################################################
