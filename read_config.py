# 用于读取.cif文件中晶格常数和原始坐标
#首先把.cif文件中的信息copy到txt文件中再进行读取
def read_config(config):
    back = dict()
    with open("%s" % config, 'r') as f:
        for line in f.readlines():
            b = line.split()
            if b[0] == '_cell_length_a':
                back['a'] = float(b[1])
            if b[0] == '_cell_length_b':
                back['b'] = float(b[1])
            if b[0] == '_cell_length_c':
                back['c'] = float(b[1])
            if b[0] == '_cell_angle_alpha':
                back['alpha'] = float(b[1])
            if b[0] == '_cell_angle_beta':
                back['beta'] = float(b[1])
            if b[0] == '_cell_angle_gamma':
                back['gamma'] = float(b[1])
        return back

def read_config1(config):
    first_element = []          # 第一元素为Al
    with open("%s" % config, 'r') as f:
        a = f.readline().split()
        aa = [a[1], a[2], a[3], a[4]]
        for i in aa:
            print('%s\n' % i)

        for line in f.readlines():
            b = line.split()
            if b[0] == a[1]:
                first_element.append([float(b[1]), float(b[2]), float(b[3])])
        return first_element

def read_config2(config):
    next_element = []  # 第二个元素为O
    with open("%s" % config, 'r') as f:
        a = f.readline().split()
        for line in f.readlines():
            b = line.split()
            if b[0] == a[3]:
                next_element.append([float(b[1]), float(b[2]), float(b[3])])
        return next_element




