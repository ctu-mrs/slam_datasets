#!/usr/bin/env python3

# import rospy
import sys, os
import numpy as np
import matplotlib.pyplot as plt
import os.path
import matplotlib.patheffects as pe
import matplotlib.ticker as ticker
from matplotlib import gridspec
import random
import math
# from pyntcloud import PyntCloud
# from pypcd import pypcd 

DATA_DIR = '..'
SAVE_PATH = os.path.join('../.fig/subt_finals.png')

DATA_SHIFT_Y = 0

# # #{ INPUT DATA
uav21_2 = {
    'transform' : {'path' : os.path.join(DATA_DIR, 'uav21_2', 'fcu_in_map.mat')},
    'cloud' : {'path' : os.path.join(DATA_DIR, 'uav21_2', 'octomap.asc'), 'color' : 'red', 'alpha' : 0.10, 'ms' : 0.01, 'downsample_ratio' : 0.6},
    'traj' : {'path' : os.path.join(DATA_DIR, 'uav21_2', 'trajectory_groundtruth.txt'), 'fg_color' : (0.7, 0.0, 0.0), 'bg_color' : 'white', 'lw' : 1.2},
}
uav21_3 = {
    'transform' : {'path' : os.path.join(DATA_DIR, 'uav21_3', 'fcu_in_map.mat')},
    'cloud' : {'path' : os.path.join(DATA_DIR, 'uav21_3', 'octomap.asc'), 'color' : 'red', 'alpha' : 0.10, 'ms' : 0.01, 'downsample_ratio' : 0.6},
    'traj' : {'path' : os.path.join(DATA_DIR, 'uav21_3', 'trajectory_groundtruth.txt'), 'fg_color' : (0.7, 0.0, 0.0), 'bg_color' : 'white', 'lw' : 1.2},
}
uav21_4 = {
    'transform' : {'path' : os.path.join(DATA_DIR, 'uav21_4', 'fcu_in_map.mat')},
    'cloud' : {'path' : os.path.join(DATA_DIR, 'uav21_4', 'octomap.asc'), 'color' : 'red', 'alpha' : 0.10, 'ms' : 0.01, 'downsample_ratio' : 0.6},
    'traj' : {'path' : os.path.join(DATA_DIR, 'uav21_4', 'trajectory_groundtruth.txt'), 'fg_color' : (0.7, 0.0, 0.0), 'bg_color' : 'white', 'lw' : 1.2},
    # 'traj' : None,
}
uav21_5 = {
    'transform' : {'path' : os.path.join(DATA_DIR, 'uav21_5', 'fcu_in_map.mat')},
    'cloud' : {'path' : os.path.join(DATA_DIR, 'uav21_5', 'octomap.asc'), 'color' : 'red', 'alpha' : 0.10, 'ms' : 0.01, 'downsample_ratio' : 0.6},
    'traj' : {'path' : os.path.join(DATA_DIR, 'uav21_5', 'trajectory_groundtruth.txt'), 'fg_color' : (0.7, 0.0, 0.0), 'bg_color' : 'white', 'lw' : 1.2},
}
uav21_6 = {
    'transform' : {'path' : os.path.join(DATA_DIR, 'uav21_6', 'fcu_in_map.mat')},
    'cloud' : {'path' : os.path.join(DATA_DIR, 'uav21_6', 'octomap.asc'), 'color' : 'red', 'alpha' : 0.10, 'ms' : 0.01, 'downsample_ratio' : 0.6},
    'traj' : {'path' : os.path.join(DATA_DIR, 'uav21_6', 'trajectory_groundtruth.txt'), 'fg_color' : (0.7, 0.0, 0.0), 'bg_color' : 'white', 'lw' : 1.2},
}

uav22_1 = {
    'transform' : {'path' : os.path.join(DATA_DIR, 'uav22_1', 'fcu_in_map.mat')},
    'cloud' : {'path' : os.path.join(DATA_DIR, 'uav22_1', 'octomap.asc'), 'color' : 'red', 'alpha' : 0.10, 'ms' : 0.01, 'downsample_ratio' : 0.6},
    'traj' : {'path' : os.path.join(DATA_DIR, 'uav22_1', 'trajectory_groundtruth.txt'), 'fg_color' : (0.7, 0.0, 0.0), 'bg_color' : 'white', 'lw' : 1.2},
    # 'traj' : None,
}
uav22_2 = {
    'transform' : {'path' : os.path.join(DATA_DIR, 'uav22_2', 'fcu_in_map.mat')},
    'cloud' : {'path' : os.path.join(DATA_DIR, 'uav22_2', 'octomap.asc'), 'color' : 'red', 'alpha' : 0.10, 'ms' : 0.01, 'downsample_ratio' : 0.6},
    'traj' : {'path' : os.path.join(DATA_DIR, 'uav22_2', 'trajectory_groundtruth.txt'), 'fg_color' : (0.7, 0.0, 0.0), 'bg_color' : 'white', 'lw' : 1.2},
    # 'traj' : None,
}
uav22_3 = {
    'transform' : {'path' : os.path.join(DATA_DIR, 'uav22_3', 'fcu_in_map.mat')},
    'cloud' : {'path' : os.path.join(DATA_DIR, 'uav22_3', 'octomap.asc'), 'color' : 'red', 'alpha' : 0.10, 'ms' : 0.01, 'downsample_ratio' : 0.6},
    'traj' : {'path' : os.path.join(DATA_DIR, 'uav22_3', 'trajectory_groundtruth.txt'), 'fg_color' : (0.7, 0.0, 0.0), 'bg_color' : 'white', 'lw' : 1.2},
}

uav24_1 = {
    'transform' : {'path' : os.path.join(DATA_DIR, 'uav24_1', 'fcu_in_map.mat')},
    'cloud' : {'path' : os.path.join(DATA_DIR, 'uav24_1', 'octomap.asc'), 'color' : 'red', 'alpha' : 0.10, 'ms' : 0.01, 'downsample_ratio' : 0.6},
    'traj' : {'path' : os.path.join(DATA_DIR, 'uav24_1', 'trajectory_groundtruth.txt'), 'fg_color' : (0.7, 0.0, 0.0), 'bg_color' : 'white', 'lw' : 1.2},
}

gt_map = {
    'cloud' : {'path' : os.path.join(DATA_DIR, 'subt_finals.asc'), 'color' : 'black', 'alpha' : 0.25, 'ms' : 0.004, 'downsample_ratio' : 0.6},
    'traj' : None,
    'transform' : None,
}
# # #}

DATASETS = [gt_map, uav21_2, uav21_3, uav21_4, uav21_5, uav21_6, uav22_1, uav22_2, uav22_3, uav24_1]
# DATASETS = [gt_map]

# # #{ quat2dcm
def quat2dcm(quaternion):
    """Returns direct cosine matrix from quaternion (Hamiltonian, [x y z w])
    """
    q = np.array(quaternion[:4], dtype=np.float64, copy=True)
    nq = np.dot(q, q)
    if nq < np.finfo(float).eps * 4.0:
        return np.identity(4)
    q *= math.sqrt(2.0 / nq)
    q = np.outer(q, q)
    return np.array((
        (1.0-q[1, 1]-q[2, 2],     q[0, 1]-q[2, 3],     q[0, 2]+q[1, 3]),
        (q[0, 1]+q[2, 3], 1.0-q[0, 0]-q[2, 2],     q[1, 2]-q[0, 3]),
        (q[0, 2]-q[1, 3],     q[1, 2]+q[0, 3], 1.0-q[0, 0]-q[1, 1])),
        dtype=np.float64)
# # #}

# # #{ dcm2quat
def dcm2quat(matrix_3x3):
    """Return quaternion (Hamiltonian, [x y z w]) from rotation matrix.
    This algorithm comes from  "Quaternion Calculus and Fast Animation",
    Ken Shoemake, 1987 SIGGRAPH course notes
    (from Eigen)
    """
    q = np.empty((4, ), dtype=np.float64)
    M = np.array(matrix_3x3, dtype=np.float64, copy=False)[:4, :4]
    t = np.trace(M)
    if t > 0.0:
        t = math.sqrt(t+1.0)
        q[3] = 0.5*t
        t = 0.5/t
        q[0] = (M[2, 1] - M[1, 2])*t
        q[1] = (M[0, 2] - M[2, 0])*t
        q[2] = (M[1, 0] - M[0, 1])*t
    else:
        i, j, k = 0, 1, 2
        if M[1, 1] > M[0, 0]:
            i, j, k = 1, 2, 0
        if M[2, 2] > M[i, i]:
            i, j, k = 2, 0, 1
        t = math.sqrt(M[i, i] - M[j, j] - M[k, k] + 1.0)
        q[i] = 0.5*t
        t = 0.5/t
        q[3] = (M[k, j] - M[j, k])*t
        q[j] = (M[i, j] + M[j, i])*t
        q[k] = (M[k, i] + M[i, k])*t
    d = np.sqrt(q[0] * q[0] + q[1] * q[1] + q[2] * q[2] + q[3] * q[3])
    return q / d
# # #}

# # #{ read_cloud()
def read_cloud(info):
    if info is None:
        return None, None

    filepath = info['path']
    print("Reading cloud from path: {}".format(filepath))
    assert os.path.exists(filepath)

    if filepath.endswith('asc'):
        return read_cloud_xyz(info)
    # elif filepath.endswith('pcd'):
    #     return read_cloud_pcd(info)
    
    print("Unknown cloud format")
    return None, None

# # #}

# # #{ read_cloud_pcd()
def read_cloud_pcd(info):

    filepath = info['path']
    # data = PyntCloud.from_file(filepath)
    data = pypcd.PointCloud.from_path(filepath)

    data = np.array(data, dtype=np.float64)
    data[:, 1] = data[:, 1] + DATA_SHIFT_Y

    if info['downsample_ratio'] is not None:
        count = data.shape[0]
        ratio = info['downsample_ratio']
        if ratio > 0 and ratio < 1:
            idx = random.sample(range(count), int(ratio * count))
            data = data[idx]
        print("- number of points: {:d}, after downsampling: {:d}".format(count, data.shape[0]))
    else:
        print("- number of points: {:d}".format(data.shape[0]))

    limits = {}
    limits['min_x'] = min(data[:, 0])
    limits['max_x'] = max(data[:, 0])
    limits['min_y'] = min(data[:, 1])
    limits['max_y'] = max(data[:, 1])
    limits['min_z'] = min(data[:, 2])
    limits['max_z'] = max(data[:, 2])

    print("- limits -> x: ({:2f}, {:2f}), y: ({:2f}, {:2f}), z: ({:2f}, {:2f})".format(limits['min_x'],  limits['max_x'], limits['min_y'], limits['max_y'], limits['min_z'], limits['max_z']))

    return data, limits
# # #}

# # #{ get_limits
def get_limits(data):
    limits = {}
    limits['min_x'] = min(data[:, 0])
    limits['max_x'] = max(data[:, 0])
    limits['min_y'] = min(data[:, 1])
    limits['max_y'] = max(data[:, 1])
    limits['min_z'] = min(data[:, 2])
    limits['max_z'] = max(data[:, 2])
    return limits
# # #}

# # #{ read_cloud_xyz()
def read_cloud_xyz(info):
    filepath = info['path']
    data = []
    with open(filepath, 'r') as f:
        
        for line in f.readlines():
            if not line.startswith('#') and not line.startswith('/'):
                line = line.split(' ') 
                data.append((line[0], line[1], line[2]))

    data = np.array(data, dtype=np.float64)
    data[:, 1] = data[:, 1] + DATA_SHIFT_Y

    if info['downsample_ratio'] is not None:
        count = data.shape[0]
        ratio = info['downsample_ratio']
        if ratio > 0 and ratio < 1:
            idx = random.sample(range(count), int(ratio * count))
            data = data[idx]
        print("- number of points: {:d}, after downsampling: {:d}".format(count, data.shape[0]))
    else:
        print("- number of points: {:d}".format(data.shape[0]))

    limits = get_limits(data)
    print("- limits -> x: ({:2f}, {:2f}), y: ({:2f}, {:2f}), z: ({:2f}, {:2f})".format(limits['min_x'],  limits['max_x'], limits['min_y'], limits['max_y'], limits['min_z'], limits['max_z']))

    return data, limits
# # #}

# # #{ read_trajectory()
def read_trajectory(info):
    if not info:
        return None

    filepath = info['path']
    print("Reading XYZ trajectory from path: {}".format(filepath))
    traj = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#') and not line.startswith('/'):
                line = line.split(' ') 
                traj.append((line[1], line[2], line[3], line[4], line[5], line[6], line[7]))

    traj = np.array(traj, dtype=np.float64)
    traj[:, 1] = traj[:, 1] + DATA_SHIFT_Y
    
    print("- number of samples: {:d}".format(traj.shape[0]))

    return traj
# # #}

# # #{ read_tf()
def read_tf(info):
    if not info:
        return None

    filepath = info['path']
    assert os.path.exists(filepath)
    print("Reading TF from path: {}".format(filepath))
    T = np.loadtxt(filepath, delimiter=' ')
    print("Transformation:\n{0}".format(T))

    return T
# # #}

# # #{ transform_trajectory()
def transform_trajectory(traj, tf):
    if tf is None or traj is None:
        return traj

    for i in range(len(traj)):
        sample = traj[i]
        T_traj = np.eye(4)
        T_traj[0:3, 3] = (sample[0], sample[1], sample[2])
        T_traj[0:3, 0:3] = quat2dcm((sample[3], sample[4], sample[5], sample[6]))
        T = tf.dot(T_traj)

        traj[i][0] = T[0, 3]
        traj[i][1] = T[1, 3]
        traj[i][2] = T[2, 3]
        q = dcm2quat(T[0:3, 0:3])
        traj[i][3] = q[0]
        traj[i][4] = q[1]
        traj[i][5] = q[2]
        traj[i][6] = q[3]

    return traj
# # #}

# # #{ transform_cloud()
def transform_cloud(cloud, tf):
    if tf is None:
        return cloud, get_limits(cloud)

    for i in range(len(cloud)):
        sample = cloud[i]
        point = np.eye(4)
        point[0:3, 3] = (sample[0], sample[1], sample[2])
        T = tf.dot(point)

        cloud[i][0] = T[0, 3]
        cloud[i][1] = T[1, 3]
        cloud[i][2] = T[2, 3]

    return cloud, get_limits(cloud)
# # #}

# # #{ plot_cloud()
def plot_cloud(ax, x_idx, y_idx, cloud, info):
    if cloud is None:
        return

    ax.scatter(cloud[:, x_idx], cloud[:, y_idx], color=info['color'], alpha=info['alpha'], marker='.', s=info['ms'])
    # ax.hexbin(cloud[:, 0], cloud[:, 1], color=info['color'], alpha=info['alpha'], gridsize=1000, mincnt=1)

# # #}

# # #{ plot_trajectory()
def plot_trajectory(ax, y_idx, traj, info):
    if traj is None:
        return

    # plt.scatter(traj[:, 0], traj[:, 1], color=color, alpha=1.0, marker='o', s=1.5)
    ax.plot(traj[:, 0], traj[:, y_idx], color=info['fg_color'], alpha=0.9, lw=info['lw'], path_effects=[pe.Stroke(linewidth=2*info['lw'], foreground=info['bg_color']), pe.Normal()])

# # #}

if __name__ == '__main__':

    for cloud_file in DATASETS:
        if 'cloud' in cloud_file and cloud_file['cloud'] is not None:
            assert os.path.exists(cloud_file['cloud']['path']), 'Cloud at ({:s}) does not exist.'.format(cloud_file['cloud']['path'])
        if 'traj' in cloud_file and cloud_file['traj'] is not None:
            assert os.path.exists(cloud_file['traj']['path']), 'Trajectory at ({:s}) does not exist.'.format(cloud_file['traj']['path'])

    params = {
              'text.usetex' : True,
              'font.size' : 10,
              'font.family' : 'lmodern',
              # 'font.weight' : 'bold',
              # 'text.latex.unicode': True,
              }
    plt.rcParams.update(params) 

    fig    = plt.figure(figsize=(12, 4), dpi=600)
    spec   = gridspec.GridSpec(ncols=1, nrows=2, height_ratios=[1, 8.78])
    ax_top = fig.add_subplot(spec[0])
    ax_bot  = fig.add_subplot(spec[1], sharex=ax_top)
    ax_top.tick_params(axis='x', bottom=False, labelbottom=False)
    # ax_bot.yaxis.set_major_locator(ticker.MultipleLocator(40))

    ax_top.grid(alpha=0.2)
    ax_bot.grid(alpha=0.2)
    ax_bot.set_xlabel('x (m)')
    ax_bot.set_ylabel('y (m)')
    
    ax_top.set_ylabel('z (m)')

    min_x = min_y = min_z = np.finfo(np.float).max
    max_x = max_y = max_z = np.finfo(np.float).min

    T_correction = np.eye(4)
    T_correction[0, 0] = 0
    T_correction[1, 1] = 0
    T_correction[0, 1] = -1
    T_correction[1, 0] = 1
    T_correction[2, 2] = 1

    for i in range(len(DATASETS)):
        pc, limits = read_cloud(DATASETS[i]['cloud'])
        traj       = read_trajectory(DATASETS[i]['traj'])
        T          = read_tf(DATASETS[i]['transform'])

        traj       = transform_trajectory(traj, T)
        pc, limits = transform_cloud(pc, T)

        traj       = transform_trajectory(traj, T_correction)
        pc, limits = transform_cloud(pc, T_correction)

        plot_cloud(ax_bot, 0, 1, pc, DATASETS[i]['cloud'])
        plot_cloud(ax_top, 0, 2, pc, DATASETS[i]['cloud'])
        plot_trajectory(ax_bot, 1, traj, DATASETS[i]['traj'])
        plot_trajectory(ax_top, 2, traj, DATASETS[i]['traj'])

        min_x = min_x if limits is None else min(min_x, limits['min_x'])
        max_x = max_x if limits is None else max(max_x, limits['max_x'])
        min_y = min_y if limits is None else min(min_y, limits['min_y'])
        max_y = max_y if limits is None else max(max_y, limits['max_y'])
        min_z = min_z if limits is None else min(min_z, limits['min_z'])
        max_z = max_z if limits is None else max(max_z, limits['max_z'])

    ax_bot.set_aspect('equal')
    ax_top.set_aspect('equal')

    ax_bot.set_ylim(ymin=-20, ymax=85)
    ax_top.set_ylim(ymin=-6, ymax=6)

    # ax_top.autoscale(False)
    # ax_bot.autoscale(False)
    
    # plt.get_current_fig_manager().full_screen_toggle()
    fig.tight_layout()
    plt.subplots_adjust(hspace=0.03)

    # plt.gcf().set_rasterized(True)
    fig.savefig(SAVE_PATH, transparent=True, bbox_inches='tight', pad_inches=0, dpi=fig.dpi, quality=100)

    fig.set_dpi(100)
    plt.show()
