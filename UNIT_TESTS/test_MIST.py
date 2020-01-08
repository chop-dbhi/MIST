from MIST import Mist, math
from random import randint

mist = Mist()
test = Mist()
mist.merge(test)

def test_MIST_Insert_5_8():
    mist.insert([5,8])
    assert mist.data == [[-math.inf, -math.inf], [5, 8], [math.inf, math.inf]]

def test_MIST_Insert_10_12():
    mist.insert([10,12])
    assert mist.data == [[-math.inf, -math.inf], [5, 8], [10, 12], [math.inf, math.inf]]

def test_MIST_Insert_2_3():
    mist.insert([2,3])
    assert mist.data == [[-math.inf, -math.inf], [2, 3], [5, 8], [10, 12], [math.inf, math.inf]]

def test_MIST_Insert_2_3():
    mist.insert([2,3])
    assert mist.data == [[-math.inf, -math.inf], [2, 3], [5, 8], [10, 12], [math.inf, math.inf]]

def test_MIST_Insert_4_4():
    mist.insert([4,4])
    assert mist.data == [[-math.inf, -math.inf], [2, 8], [10, 12], [math.inf, math.inf]]

def test_MIST_Insert_4_6():
    mist.insert([4,6])
    assert mist.data == [[-math.inf, -math.inf], [2, 8], [10, 12], [math.inf, math.inf]]

def test_MIST_Insert_12_14():
    mist.insert([12 , 14])
    assert mist.data == [[-math.inf, -math.inf], [2, 8], [10, 14], [math.inf, math.inf]]

def test_MIST_Insert_12_13():
    mist.insert([12, 13])
    mist.insert([12, 12])
    assert mist.data == [[-math.inf, -math.inf], [2, 8], [10, 14], [math.inf, math.inf]]

def test_MIST_Insert_3_20():
    mist.insert([3, 20])
    assert mist.data == [[-math.inf, -math.inf], [2, 20],  [math.inf, math.inf]]

def test_MIST_Insert_24_24():
    mist.insert([24, 24])
    assert mist.data == [[-math.inf, -math.inf], [2, 20], [24, 24],  [math.inf, math.inf]]

def test_MIST_Insert_21_23():
    mist.insert([21, 23])
    assert mist.data == [[-math.inf, -math.inf], [2, 24], [math.inf, math.inf]]                

def test_MIST_Insert_30_31():
    mist.insert([30, 31])
    assert mist.data == [[-math.inf, -math.inf], [2, 24], [30, 31], [math.inf, math.inf]]    

def test_MIST_Insert_31_31():
    mist.insert([31, 31])
    assert mist.data == [[-math.inf, -math.inf], [2, 24], [30, 31], [math.inf, math.inf]]   

def test_MIST_Intersects_1():
    assert mist.intersects(1) == False 

def test_MIST_Intersects_1_3_():
    assert mist.intersects([1,1,1,1,3]) == True 

def test_MIST_Intersects_1_25_32():
    assert mist.intersects([1,1,1,1,25,32]) == False 

def test_MIST_Intersects_1_25_31():
    assert mist.intersects([1,1,1,1,25,31]) == True     

def test_MIST_Intersects_1_25_big():
    assert mist.intersects([0, 100, 1000000000, 2]) == True     

def test_MIST_Intersects_1_25_big2():
    assert mist.intersects([0, 100, 1000000000, 1]) == False

def test_MIST_Merge():
    test = Mist()
    test.merge(mist)
    assert test.data == [[-math.inf, -math.inf], [2, 24], [30, 31], [math.inf, math.inf]]   

def test_MIST_Merge_Large():
    mist1 = Mist()
    mist2 = Mist()
    for j in range(0,10):
        mist1.insert([j*10,j*10+8])
    for j in range(0,10):
        mist2.insert([j*10+9,j*10+9])
    mist1.merge(mist2)
    assert mist1.data == [[-math.inf, -math.inf], [0, 99], [math.inf, math.inf]] 

def test_MIST_DEEP_True():
    def test_MIST_DEEP_Internal(n=200 ,state=True,lst=[],mist=Mist()):
        if n == 0:
            return state
        n -= 1;
        d = randint(0,1e6)
        f = randint(0,1e3)
        mist.insert([d,d+f])    
        for z in range(d,d+f):
            state = state & mist.intersects(z)
        return test_MIST_DEEP_Internal(n,state,lst,mist) 
    assert test_MIST_DEEP_Internal() == True













