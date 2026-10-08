# Project Report - Network Routing

## Baseline

### Design Experience
I met w/ Dexter Brunt. 
- Do I understand the provided framework?
    - dict[int, dict[int, float]] this means its a dictionary of dictionaries. To find the cost of edge from node_1 to node_2, look it up using graph[node_1][node_2]
    - and then main.py runs everthing and network_routing.py is where we impletent it
- Do I understand how Dijkstra's algorithm works?
    - yes the psuedo code is

        init source node distance to 0, other nodes to inf
        init a structure to track the previous node for each node
        add all nodes to lpq

        loop while lpq is not empty:
            current = pop.lpq.lowest

            if current is the target node:
                break
                
            look at current's vecinos:
                for each vecino:
                    new_path_distance =
                        (distance to current) + (edge weight from current to vecino)
                    
                    if(new_path_distance < the vecino's currently recorded distance):
                        vecino's distance=new_path_distance
                        update the vecino's distance in the lpq 
                        record that the vecino's previous node is current # this is to record the path of the node all the way
            

- Can I do it by hand correctly?   
    - yes
- Can I explain it to someone else?
    - yes

- Do I understand how the linear priority queue works?
    - yes. We are using a dictionary based lpq. Not FIFO, its lowest nuumber goes first. But we store them linearly, so its not sorted, its not random access, so to get an element its linear time, thus the name. Key is the node id, value is the starting distance. 
- How would I implement the following functions work?

    - insert - again Key is the node id, value is the starting distance. just add a new key-value pair to the dictionary. Python dicionary's add is instant time. 
    - delete min - look at every node, track what the lowest one is. takes V time. 
    - decrease key - when we find a loop that is faster, the old one gets replaced by this new one, thats random access because we already know the node. 

- What data structures will I use for my algorithm? 
    - dictionary for the lpq, 
- What are the pros and cons of those algorithms?
    - as mentioned above the lpq is not sorted, so to find the smallest value, you have to loop through it every time. 
- What file will I put my priority queue implementation in?
    - network routing
- How will my design decisions for my linear PQ affect my core implementation?
    - Core is asking for a binary heap for the priority queue. This means there will be changes to the code between cores, but if you decouple the code from eachother and use some objects, we only should have to rewrite the implementation of teh priority queue. 

- How can I avoid significant code duplication for the core tier?
    - Again, we don't have to rewrite the alrgorithm. We should just write the new data structure and use that. 

- What is the expected time and space complexity of my algorithm? 
    - if delete min is O(V) and insert and decrease key are O(1) then its bigO(v^2) cause we can loop up to v times. 
    - for space complexity its v + e, we just have to keep the space for each one 

### Theoretical Analysis - Dijkstra's With Linear PQ

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data - Dijkstra's With Linear PQ

| V    | Density | time (sec) |
|------|---------|------------|
| 500  | .2      |            |
| 1000 | .2      |            |
| 1500 | .2      |            |
| 2000 | .2      |            |
| 2500 | .2      |            |
| 3000 | .2      |            |
| 3500 | .2      |            |

### Comparison of Theoretical and Empirical Results - Dijkstra's With Linear PQ

- Theoretical order of growth: *copy from section above* 
- Empirical order of growth (if different from theoretical): 


![img](img.png)

*Fill me in*

## Core

### Design Experience

*Fill me in*

### Theoretical Analysis - Dijkstra's With Heap PQ

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data - Dijkstra's With Heap PQ

| V    | Density | time (sec) |
|------|---------|------------|
| 500  | .2      |            |
| 1000 | .2      |            |
| 1500 | .2      |            |
| 2000 | .2      |            |
| 2500 | .2      |            |
| 3000 | .2      |            |
| 3500 | .2      |            |



### Comparison of Theoretical and Empirical Results - Dijkstra's With Heap PQ

- Theoretical order of growth: *copy from section above* 
- Empirical order of growth (if different from theoretical): 

![img](img.png)

*Fill me in*

### Relative Performance Of Linear versus Heap PQ Performance

*Fill me in*

## Stretch 1

### Design Experience

*Fill me in*

### Empirical Data

| V    | Density | heap time (sec) | linear PQ time (sec) |
|------|---------|-----------------|----------------------|
| 500  | .6      |                 |                      |
| 1000 | .6      |                 |                      |
| 1500 | .6      |                 |                      |
| 2000 | .6      |                 |                      |
| 2500 | .6      |                 |                      |
| 3000 | .6      |                 |                      |
| 3500 | .6      |                 |                      |


| V    | Density | heap time (sec) | linear PQ time (sec) |
|------|---------|-----------------|---------------------|
| 500  | 1       |                 |                     |
| 1000 | 1       |                 |                     |
| 1500 | 1       |                 |                     |
| 2000 | 1       |                 |                     |
| 2500 | 1       |                 |                     |
| 3000 | 1       |                 |                     |
| 3500 | 1       |                 |                     |

### Plot

*Fill me in*

### Discussion

*Fill me in*

## Stretch 2

### Design Experience

*Fill me in*

### Provided Graph Generation Algorithm Explanation

*Fill me in*

### Selected Graph Generation Algorithm Explanation

*Fill me in*

#### Screenshots of Working Graph Generation Algorithm

![img](small.png)

![img](medium.png)

![img](large.png)

## Project Review

*Fill me in*

