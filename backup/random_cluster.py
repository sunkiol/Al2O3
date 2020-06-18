# 用于按原子比例生成随机大小的Al2O3团簇
# 计算al-al，o-o，al-o之间最小距离
# 由于MS中氧化铝各键长不同，在随机选取原子的时候，将最小半径乘以1.4
import random
import math


def random_cluster(al, o):
    a = int(input('please input nums of Al2O3::'))
    alnums = 2 * a
    alnums_want = 10 * alnums
    onums = 3 * a
    onums_want = 10 * onums
    all_num = alnums + onums
    al_want = al[:alnums_want]
    o_want = o[:onums_want]

    r_al = 10000
    r_o = 10000
    r_alo = 10000

# 计算o-o, al-al, al-o之间最小的距离：
    for i in range(len(al_want)):
        ii = i + 1
        for k in range(ii, len(al_want)):
            dx = al[ii][0] - al[i][0]
            dy = al[ii][1] - al[i][1]
            dz = al[ii][2] - al[i][2]
            ral = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
            if r_al > ral:
                r_al = ral
    for i in range(len(o_want)):
        jj = i + 1
        for j in range(jj, len(o_want)):
            dx = o[jj][0] - o[i][0]
            dy = o[jj][1] - o[i][1]
            dz = o[jj][2] - o[i][2]
            ro = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
            if r_o > ro:
                r_o = ro
    for i in range(len(al_want)):
        for l in range(len(o_want)):
            dx = al[i][0] - o[l][0]
            dy = al[i][1] - o[l][1]
            dz = al[i][2] - o[l][2]
            ralo = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
            if r_alo > ralo:
                r_alo = ralo
    print('r_alo: %f' % r_alo)
# 取随机的Al和o的坐标
    candidate_o = []
    candidate_al = []
    o_backup = []
    al_backup = []
    o_random = []
    al_random = []
    al_choice = []
    o_choice = []

    # 在原点附近找到第一个o原子
    for i in o_want:
        dist = math.sqrt(i[0] ** 2 + i[1] ** 2 + i[2] ** 2)
        if dist < 2 * r_o:
            candidate_o.append(i)
    o_random.append(random.choice(candidate_o))
    candidate_o.clear()
    # 找到o原子附近的al
    alnum = 1
    onum = 2
    while onum <= onums:
        if alnum <= alnums:
            for j in range(len(al_want)):
                k = len(o_random) - 1
                ddx = al_want[j][0] - o_random[k][0]
                ddy = al_want[j][1] - o_random[k][1]
                ddz = al_want[j][2] - o_random[k][2]
                rrr = math.sqrt(ddx ** 2 + ddy ** 2 + ddz ** 2)
                if rrr < 1.4 * r_alo:
                    aaa = al_want[j]
                    if aaa not in al_random:
                        candidate_al.append(aaa)
            print('candidate', candidate_al)
            if len(candidate_al) > 0:
                for i in candidate_al:
                    if i in al_backup:
                        al_choice.append(i)
                if len(al_choice) > 0:
                    aa = random.choice(al_choice)
                else:
                    aa = random.choice(candidate_al)
                al_random.append(aa)
                if aa in candidate_al:
                    candidate_al.remove(aa)
                else:
                    print('candidate:', candidate_al)
                    raise ValueError('aa:', aa, 'not in candidate')
                for i in candidate_al:
                    if i not in al_backup:
                        al_backup.append(i)
            else:
                if len(al_backup) == 0:
                    raise ValueError('there are no nearby Al atoms')
                else:
                    aa = random.choice(al_backup)
                    al_random.append(aa)                                # 选中随机Al原子坐标
            candidate_al.clear()
            alnum += 1

        for i in range(len(o_want)):
            l = len(al_random) - 1
            dx = o_want[i][0] - al_random[l][0]
            dy = o_want[i][1] - al_random[l][1]
            dz = o_want[i][2] - al_random[l][2]
            rr = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
            if rr < 1.4 * r_alo:
                aaaa = o_want[i]
                if aaaa not in o_random:
                    candidate_o.append(aaaa)
        if len(candidate_o) > 0:
            for i in candidate_o:
                if i in o_backup:
                    o_choice.append(i)
            if len(o_choice) > 0:
                bb = random.choice(o_choice)
            else:
                bb = random.choice(candidate_o)
            al_random.append(bb)
            if bb in candidate_o:
                candidate_o.remove(bb)
            else:
                print('candidate:', candidate_o)
                raise ValueError('bb:', bb, 'not in candidate')
            for i in candidate_o:
                if i not in o_backup:
                    o_backup.append(i)
        else:
            if len(o_backup) == 0:
                raise ValueError('there are no nearby o atoms')
            else:
                bb = random.choice(o_backup)
                o_random.append(bb)                                    # 选中随机O原子坐标
        candidate_o.clear()
        onum += 1
    return al_random, o_random, all_num


