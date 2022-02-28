Public datasets[^1] for research on laser-based SLAM or localization.

## Folder structure
```
slam_datasets
│   download.sh
└───bull_rock_cave
└───subt_finals
└───...
```
- To download the datasets, run script `download.sh [datasets]`.
  - **Beware**, the datasets can be large!
  - Datasets can be downloaded by specifying a comma-separated list of datasets: `./download.sh "bull_rock_cave,subt_finals"`
  - All datasets will be downloaded if no argument is given.

## Datasets
- [Bull Rock Cave](./bull_rock_cave/README.md)
- [DARPA Subterranean Challenge](./descriptions/darpa_subt.md)

[^1]: Datasets are stored on internal MRS [NAS](https://nasmrs.felk.cvut.cz/index.php/apps/files/?dir=/shared/PERMANENT/slam_datasets&fileid=2620203).
