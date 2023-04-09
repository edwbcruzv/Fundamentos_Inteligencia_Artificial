import numpy as np
if __name__ == '__main__':
    m = np.zeros((15, 15), dtype=int)

    np.savetxt('Renombrar.txt', m, fmt='%d')
    # print(m)
    # print(m.shape)
    # print(type(m))
