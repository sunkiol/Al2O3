# -*- coding:utf-8 -*-
# Institution: AnHui University Professor Cheng group
# Location: G304
# Purpose: Finding Al2O3 cluster in crystal
# Author: Sun ji

import expandcoor
import read_config
import random_cluster
import energy
import time
from expandcoor import addcoor
from read_config import read_config
from read_config import read_config1
from read_config import read_config2
from random_cluster import random_cluster
if __name__ == '__main__':
    # t_start = time.time()
    # 读取配置文件
    AL = read_config1('mp-2254.txt')
    O = read_config2('mp-2254.txt')
    aa = read_config('mp-2254.txt')
    alpha = aa['alpha']
    beta = aa['beta']
    gama = aa['gamma']
    a = aa['a']
    b = aa['b']
    c = aa['c']

    # 真实的三维坐标
    AL_real = []
    O_real = []
    for i in AL:
        x = i[0] * a
        y = i[1] * b
        z = i[2] * c
        AL_real.append([x, y, z])
    for i in O:
        x = i[0] * a
        y = i[1] * b
        z = i[2] * c
        O_real.append([x, y, z])
    # 调用函数扩展坐标
    AL_add = addcoor(a, b, c, AL_real)
    O_add = addcoor(a, b, c, O_real)

    # 将扩展的坐标写入xyz文件中
    ALnum = len(AL_add)
    Onum = len(O_add)
    Atomnum = ALnum + Onum
    with open("mp-2254-exp.xyz", 'w') as f:
        f.write(str(Atomnum)+'\n')
        f.write("AL  " + str(ALnum) + "  " + "O  " + str(Onum) + "\n")
        for i in AL_add:
            f.write("Al" + "  " + str(i[0]) + "  " + str(i[1]) + "  " + str(i[2]) + "\n")
        for i in O_add:
            f.write("O" + "  " + str(i[0]) + "  " + str(i[1]) + "  " + str(i[2]) + "\n")

    # 随机生成想要大小的团簇：

    (Al_coor, O_coor, lattice_Al, lattice_O, molecule_num, r_alo) = random_cluster(AL_add, O_add)
    '''with open("random_cluster.xyz", 'w') as f:
        f.write(str(molecule_num) + '\n')
        f.write('Al2O3' + '\n')
        for i in Al_coor:
            f.write("Al" + "  " + str(i[0]) + "  " + str(i[1]) + "  " + str(i[2]) + "\n")
        for i in O_coor:
            f.write("O" + "  " + str(i[0]) + "  " + str(i[1]) + "  " + str(i[2]) + "\n")
    # t_end = time.time()
    # T = t_end - t_start
    # print('cost time:%f' % T)'''
    with open('latitice.xyz', 'w') as f:
        lattice_num = len(lattice_Al) + len(lattice_O)
        f.write(str(lattice_num) + '\n')
        f.write('lattice coor' + '\n')
        for i in lattice_Al:
            f.write("Al" + "  " + str(i[0]) + "  " + str(i[1]) + "  " + str(i[2]) + "\n")
        for i in lattice_O:
            f.write("O" + "  " + str(i[0]) + "  " + str(i[1]) + "  " + str(i[2]) + "\n")

    # 计算团簇能量：

