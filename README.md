## Paper Title

Sequential Trajectory Data Publishing with Differential Privacy

## Introduction

In this paper, we propose a probability distribution based model named DP-STP (Differentially Private Sequential Trajectory Publishing) which satisfies differential privacy while publishing sequential trajectory data with high utility.

## Framework

The framework includes three layers: data layer, logical layer and application layer. In data layer, we clean the original trajectory dataset with three filters to sample data with specific range of time, location and scale. Besides, we choose the shortest description data as the representative points by adopting Minimum Description Length (MDL) to simplify the dataset. In logical layer, firstly, we design a multilevel adaptive grid structure to discretize spatial domain. Rather than just one or two levels, the grid structure we designed is multilevel which could refine dense area better. The grid structure is data adaptive that we needn’t set the grid configuration according to the specified dataset features. Secondly, DP-StarM generates a rebuilt trajectory dataset by adopting specific steps in DP-Star. Thirdly, we present a two-stage postprocessing method, which is based on direction and density of trajectory to optimize generatedtrajectory. Specifically, the last trajectory point is added to the penultimate trajectory point directly in DP-Star that may lead to unreasonable deviation of direction. Based on direction- and density-based postprocessing, we design an outlier processing algorithm to remove and map the outliers in order to make trajectories with more utility. In application layer, we present visalization and some potential applications.

<img src="https://i.loli.net/2021/06/16/kdwnm1rRFDy7AEt.png" alt="fig-framework.png"  />

**The procedure of DP-STP is as follows：**

1. Data Clean；
2. Representative Point Identification；
3. Multilevel Adaptive Grid Construction；
4. Trip Distribution Extraction；
5. Mobility Model Construction；
6. Route Length Estimation；
7. Synthetic Trajectory Generation；
8. Post-Processing；
   - Direction-based Processing；
   - Density-based Processing；

## Requirements

To install requirements：

`pip install -r requirements.txt`

Python Version：3.7.7

## Instruction

Because we encapsulate the program, if you have a clean trajectory data, you can directly run `main.py` to execute all the remaining processes of DP-STP. But in order to better understand the code execution process, I will introduce their steps one by one.

#### Data Clean

Set a sampling frequency, sampling range and sampling scale to filter the original trajectory data to get a cleaned trajectory data. The format of a cleaned trajectory is as follows：

```
cleaned_trajectory_1.txt

39.984702,116.318417
39.984683,116.31845
39.984686,116.318417
39.984688,116.318385
39.984655,116.318263
39.984611,116.318026
39.984608,116.317761
...
```

#### Representative Point Identification

`dp_stp/mdl.pt` is to simplify the trajectories so as to obtain representative points that can summarize each trajectories.

The trajectory after `mdl.py` is：

```
mdled_trajectory_1.txt

(558.1554000000046, 737.0187000000016)
(557.5504000000002, 738.2044999999935)
(557.8726999999993, 739.7521999999938)
(558.2357000000052, 740.9225999999933)
(556.7616999999984, 742.7837999999995)
(556.6770000000013, 746.4709999999911)
(556.7462999999982, 749.0405999999907)
...
```

#### Multilevel Adaptive Grid Construction

`dp_stp/multi_level_adaptive_grid_construction.py` is for getting the **grid structure**, **grid tree** and the **grid trajectory**.

> Example：
>
> grid structure：Middleware/grid_tree_list_epsilon.txt
>
> grid tree：Middleware/grid_tree_epsilon.pkl
>
> grid trajectory：Middleware/grid_trajs_epsilon.txt

The format of grid trajectory is：

```
grid_trajectories.txt

[18, 18, 15, 15, 15, 15, 31, 31, 31, 33, 39, 39, 42, 42, 43, 43, 43, 65, 67, 68]
[83, 151, 151, 72, 72, 72, 143, 143, 142, 142, 71, 71, 68, 71, 71, 69, 69, 69]
[115, 115, 109, 109, 109, 107, 45, 45, 67, 68, 68, 68, 69, 69, 69, 68, 69, 70, 70, 81, 83, 84]
[115, 115, 115, 109, 108, 108, 108, 108, 106, 106, 107, 107, 106, 106, 106, 106, 103]
[57, 58, 58, 50, 19, 50, 19, 19, 36, 36, 36, 42, 44, 106, 106, 108, 108, 108, 108]
[161, 161, 161, 161, 161, 161, 158, 158, 158, 158, 149, 146, 109]
[64, 63, 63, 63, 63, 64, 64, 64, 70]
...
```

#### Trip Distribution Extraction

`dp_stp/trip_distribution_extraction.py` is to obtain the probability distribution matrix of the start and end points of the trajectory.

#### Mobility Model Construction

`dp_stp/mobility_model_construction.py` is to obtain the probability transfer matrix of the middle point of the trajectory.

#### Route Length Estimation

`dp_stp/route_length_estimation.py` uses the median mechanism to estimate the length of each trajectory.

#### Synthetic Trajectory Generation

`dp_stp/synthetic_trajectory_generation.py` combines the results of `Multilevel Adaptive Grid Construction`, `Trip Distribution Extraction`, `Mobility Model Construction` and `Route Length Estimation` to generate a desensitization trajectory data.

#### Post-Processing

##### Direction-based Processing

`dp_stp/prune_by_direction.py` is to divide the location domain into normal region, mapping region and deletion region. The trajectory points in the mapping area and the deletion area are identified as abnormal points, and the trajectory points in the normal area are identified as normal points. When the outlier is in the mapping area, it is mapped to the line connected with its front and back points, otherwise it will be deleted.

`dp_stp/prune_by_density.py` is to test every point in the trajectory with the same start and end points. If there is a big deviation between a point and most points in the trajectory with the same start and end points, it will be regarded as an abnormal point and deleted.

