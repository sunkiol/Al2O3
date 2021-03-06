
# 用于立方晶胞结构，扩展原子倍数，并产生扩展原子坐标
# num = 256
#
# 将原来的晶胞扩展到256倍
import math
def dist(x):
    distance = math.sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2)
    return distance

def addcoor(a, b, c, coor):
    expcoor = []            # 用于拓展原始晶胞
    # if alpha == 90 & beta == 90 & gama == 90:   # 仅适用于立方体
    if True:
        for i in range(0, len(coor)):                                           # 将coor的坐标复制到expcoor
            expcoor.append([coor[i][0], coor[i][1], coor[i][2]])

        count = 1
        while count <= 6:                                                       # 将expcoor坐标沿X正方向扩展三倍
            for i in range(0, len(coor)):
                expcoor.append([coor[i][0] + count * a, coor[i][1], coor[i][2]])
            count += 1

        expcoor_length = len(expcoor)                                           # 将expcoor坐标扩展成Y轴对称
        for i in range(0, expcoor_length):
            expcoor.append([expcoor[i][0] - 4 * a, expcoor[i][1], expcoor[i][2]])

        count1 = 1                                                              # 将expcoor坐标沿Y正方形扩展三倍
        expcoor_length1 = len(expcoor)
        while count1 <= 3:
            for i in range(0, expcoor_length1):
                expcoor.append([expcoor[i][0], expcoor[i][1] + count1 * b, expcoor[i][2]])
            count1 += 1

        expcoor_length2 = len(expcoor)                                          # 将expcoor坐标扩展成X轴对称
        for i in range(0, expcoor_length2):
            expcoor.append([expcoor[i][0], expcoor[i][1] - 4 * b, expcoor[i][2]])

        count2 = 1                                                              # 将expcoor坐标沿Z轴正方向扩展三倍
        expcoor_length3 = len(expcoor)
        while count2 <= 3:
            for i in range(0,expcoor_length3):
                expcoor.append([expcoor[i][0], expcoor[i][1], expcoor[i][2] + count2 * c])
            count2 += 1

        expcoor_length4 = len(expcoor)                                          # 将坐标扩展成xy面对称
        for i in range(0, expcoor_length4):
            expcoor.append([expcoor[i][0], expcoor[i][1], expcoor[i][2] - 4 * c])

    adjcoor = []            # 用于去除重复的坐标
    ii = 0
    while ii < len(expcoor):
        if expcoor[ii] not in adjcoor:
            adjcoor.append(expcoor[ii])
        else:
            ii += 1
    sortcoor = []    # 用于排序，按照距离原点距离进行排序，#暂时没有分别的(x+,y+,z+),(x-,y+,z+),(x-,y-,z+),(x+,y-,z+)及z-
    sortcoor = sorted(adjcoor, key=dist)

    return sortcoor
