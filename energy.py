# 用于计算团簇的能量

import math

def potential_enengy_fun(a, b, c, d, e, f):
    # V(rij) = qi*qj/rij + A/rij**12 + B*exp(-rij/p) - C/rij**6
    # a=qi,b=qj,c=rij,d=A,e=B,f=p,其中如果只考虑Al-O作用，C=0
    v = (a * b)/c + d/(c ** 12) + e * math.exp((-c)/f)
    return v

def cluster_total_energy(al, o, r_alo):
    q_al, q_o = 3, -2
    a, b, p = 10.0, 2409.505, 0.2649
    energy_list = []
    for i in al:
        for j in o:
            r = math.sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2 + (i[2]-j[2])**2)
            if r <= 2 * r_alo:
                energy = potential_enengy_fun(q_al, q_o, r, a, b, p)
                energy_list.append(energy)




