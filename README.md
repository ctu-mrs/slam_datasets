Public datasets[^1] for research on laser-based SLAM, localization and mapping.

## Folder structure
```
slam_datasets
│   download.sh
├───bull_rock_cave
├───subt_finals
└───forest
```
- To download the datasets, run script `download.sh [datasets]`.
  - **Beware**, the datasets can be large!
  - Datasets can be downloaded by specifying a comma-separated list of datasets:
    - `./download.sh "bull_rock_cave,subt_finals"`
  - All datasets will be downloaded if no argument is given.

## Datasets
- [Bull Rock Cave](./bull_rock_cave/README.md) [1]
- [DARPA Subterranean Challenge](./subt_finals/README.md) [1, 2]

## References
- [1] Petracek, P.; Kratky, V.; Petrlik, M.; Baca, T.; Kratochvil, R.; Saska, M. *Large-Scale Exploration of Cave Environments by Unmanned Aerial Vehicles,* IEEE Robotics and Automation Letters 2021, 6, 7596–7603.
- [2] V. Kratky, P. Petracek, T. Baca and M. Saska, *An autonomous unmanned aerial vehicle system for fast exploration of large complex indoor environments,* Journal of field robotics, May 2021.
 
[^1]: Datasets are stored on internal MRS [NAS](https://nasmrs.felk.cvut.cz/index.php/apps/files/?dir=/shared/PERMANENT/slam_datasets&fileid=2620203).
