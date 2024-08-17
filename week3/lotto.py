import numpy as np
import random

__author__ = '장은선'
__version__ = '0.1.0'
__license__ = '덕성여자대학교'

def make_lotto_sp(count):
    for i in range(count):
        lotto_num = random.sample(range(1, 45), 6)

        lotto_num.sort()
        print("{}. 로또번호: {}".format(i+1, lotto_num))
        
def make_lotto_rd(count):
    for i in range(count):
        lotto_num = []

        for j in range(6):
            rand_num = random.randint(1, 46)
            lotto_num.append(rand_num)

        lotto_num.sort()
        print("{}. 로또번호: {}".format(i+1, lotto_num))
        
def make_lotto_np(count):
    for i in range(count):          
        lotto_num = np.random.choice(range(1, 46), 6, replace=False)

        lotto_num.sort()
        print("{}. 로또번호: {}".format(i+1, lotto_num))


def main():
    count = int(input("로또 번호를 몇개 생성할까요?> "))
    
    make_lotto_np(count)
    #make_lotto_rd(count)
    #make_lotto_sp(count)
    
    print("로또 번호 %d 개를 생성했습니다." % count)

if __name__ == '__main__':
    main()