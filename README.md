# Entropy Based Graph Clustering (EBGC)

This is an python implementation of Entropy Based Graph Clustering. 

Paper: [Entropy-Based Graph Clustering: Application to Biological and Social Networks](http://cse.iitrpr.ac.in/ckn/courses/f2012/xiyu.pdf)

**Remark**

1. This repository is not the official release.

2. If you find this repository useful, please star this repository  and cite the following paper:

   ```
   @INPROCEEDINGS{6137324,  author={E. C. {Kenley} and Y. {Cho}},  booktitle={2011 IEEE 11th International Conference on Data Mining},   title={Entropy-Based Graph Clustering: Application to Biological and Social Networks},   year={2011},  volume={},  number={},  pages={1116-1121},}
   ```

   

## Requirement

- Python 3.6
- numpy 1.15.1
- networkx 2.1
- matplotlib 2.2.2

## Demo Result

1. **Demo Graph**

   To  demonstrate the algorithm, we build a demo graph.

   Graph Clustering Result

   ![fig1](.\result\fig1.png)

    Cluster Result

   ![fig1_cluster](.\result\fig1_cluster.png)

2. **NCI1 Dataset**
   We also perform the algorithm at NC1 dataset.

   Graph Clustering Result

   ![fig2](.\result\fig2.png)

   Cluster Result

   ![fig2_cluster](.\result\fig2_cluster.png)

## Usage

```python
from EBGC import EBGC 

# demo_graph should be a graph of networkx
EBGC_cluster = EBGC()
cluster_result = EBGC_cluster.fit(demo_graph)
# the cluster result is a n*c array, where n denotes the number of nodes and c denotes the number of clusters. If V_i belongs to C_j, then the elements of cluster_result e_ij = 1.
```





