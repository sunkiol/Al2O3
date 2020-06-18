
# 计算al-o之间最小距离
import random
import math


def random_cluster(al, o):
    # 首先需要得到多少个al2o3分子，并确定al和o的原子数量:
    al2o3 = int(input('how many al2o3 molecule:'))
    al_num = 2 * al2o3      # 所需al原子数
    o_num = 3 * al2o3       # 所需o原子数
    all_num = al_num + o_num
    # 取出所需要原子数的坐标:
    al_coor = al[:al_num]   # 所需al坐标
    o_coor = o[:o_num]      # 所需o坐标

    # 取两倍原子数坐标，用于后续寻找格点:
    al_more = al[al_num:2 * al_num]
    o_more = o[o_num:2 * o_num]

# 计算al-o最小键长：
    r_alo = 100  # 假定长度
    for i in al_coor:
        for j in o_coor:
            dx = i[0] - j[0]
            dy = i[1] - j[1]
            dz = i[2] - j[2]
            dists = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
            if dists <= r_alo:
                r_alo = dists
    print('r_alo:', r_alo)      # r_alo及为最小al_o长度

# 寻找格点坐标：
    # o原子格点选择[最外面的o，最外面的al+2*r_alo]距离的o
    # al和o的坐标都是按照距离[0,0,0]排序好的

    rmax_al = math.sqrt(al_coor[al_num-1][0] ** 2 + al_coor[al_num-1][1] ** 2 + al_coor[al_num-1][2] ** 2)
    rmax_o = math.sqrt(o_coor[o_num-1][0] ** 2 + o_coor[o_num-1][1] ** 2 + o_coor[o_num-1][2] ** 2)

    # 格点坐标分别为lattice_al, latiice_o
    lattice_al = []
    lattice_o = []

    # 判断rmax_al和rmax_o大小
    if rmax_al < rmax_o:
        # al格点范围[rmax_al,rmax_o+2*r_alo]
        for i in al_more:
            dists1 = math.sqrt(i[0] ** 2 + i[1] ** 2 + i[2] ** 2)
            if dists1 <= (rmax_o + 2 * r_alo):
                lattice_al.append(i)
        # o格点范围[rmax_o,rmax_o+2*r_alo]
        for i in o_more:
            dists2 = math.sqrt(i[0] ** 2 + i[1] ** 2 + i[2] ** 2)
            if dists2 <= (rmax_o + 2 * r_alo):
                lattice_o.append(i)
    else:
        # al格点范围[rmax_al,rmax_al+2*r_alo]
        for i in al_more:
            dists1 = math.sqrt(i[0] ** 2 + i[1] ** 2 + i[2] ** 2)
            if dists1 <= (rmax_o + 2 * r_alo):
                lattice_al.append(i)
        # o格点范围[rmax_o,rmax_al+2*r_alo]
        for i in o_more:
            dists2 = math.sqrt(i[0] ** 2 + i[1] ** 2 + i[2] ** 2)
            if dists2 <= (rmax_o + 2 * r_alo):
                lattice_o.append(i)
    return al_coor, o_coor, lattice_al, lattice_o, all_num, r_alo
