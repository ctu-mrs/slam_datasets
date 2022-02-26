#!/usr/bin/env python3

import os
import argparse

from scipy.spatial.transform import Rotation as R

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='''Parse origin from a trajectory file''')
    parser.add_argument('trajectory_in', help='Input trajectory')
    parser.add_argument('matrix_out', help='Output matrix')
    args = parser.parse_args()

    origin=None
    with open(args.trajectory_in) as traj:
        for line in traj.readlines():
            if not line.startswith('#'):
                elements = line.split(' ')
                if len(elements) == 8:
                    origin = (elements[1], elements[2], elements[3], elements[4], elements[5], elements[6], elements[7])
                    break

    if not origin:
        print('Origin not found')
        exit( -1)

    t   = (origin[0], origin[1], origin[2])
    q   = R.from_quat([origin[3], origin[4], origin[5], origin[6]])
    mat = q.as_matrix()

    print('Writing transformation matrix to: ', args.matrix_out)
    with open(args.matrix_out, "w") as tf:
        lines = []
        for i in (0, 1, 2):
            lines.append(''.join([str(mat[i, 0]), ' ', str(mat[i, 1]), ' ', str(mat[i, 2]), ' ', str(t[i]), '\n']))
        lines.append(''.join([str(0), ' ', str(0), ' ', str(0), ' ', str(1)]))
        tf.writelines(lines)

    exit(0)
