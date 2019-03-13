# Abstract

In taxi ride-sharing, multiple customers are allotted to the same taxi as long as they are *compatible*, i.e., if none of them suffers a detour beyond a permissible threshold. To attract customers to ride-sharing, taxi operators promise a reduced fare upfront. As a result, if the taxi fails to pair the initial customer with additional compatible passengers, the taxi operator incurs a financial loss. Hence, it is important to ensure that the taxi finds compatible customers once it has picked up the initial customer. In the current scenario, the appearance of subsequent compatible customers is left to luck: a taxi moves along the shortest (or quickest) path for the existing customer and hopes to find additional compatible customers on its way. In this paper, we ask: *Is the shortest path the optimal path for ride-sharing?* To investigate this question, we develop a route recommendation algorithm called **SHARE**, which predicts the route with the highest probability of finding compatible customers, while staying within the detour limits. Through extensive evaluations on real datasets, we show that **SHARE** reduces failure rate in ride-sharing by up to 40%, while also improving waiting time for customers by 20%. Technically, the route recommendation problem is NP-hard. We overcome this bottleneck, by reducing the search space of the entire road network into a smaller directed acyclic graph, on which we perform *dynamic programming* to identify the optimal route. This strategy allows us to answer queries within 0.2 seconds, and thereby making **SHARE** deployable on real road conditions. 


# SHARE
This project can be run on any city map and we have experimented and testes on the data for the cities: Singapore, New York and San Francisco

## Steps to run the project
1. Download the Data Set for the city for which you want to run the simulation from the following link: 
    https://drive.google.com/drive/folders/1DiVSOqANI3Ww0jHSKMw5VcxH04aIJsHC?usp=sharing

2. Keep all the data files in the 'main' folder as that of all the other code.

3. To compile the Project run: 
    ```
    g++ -O3 -std=c++11 realtimesimulation.cpp Hungarian.cpp
    ```
  
    This will generate the 'a.out' file and then execute it with parameters.
    
4. To run :
    Usage: 
    ```
    ./a.out [location={SF|NY|SG}] [alpha=1.3] [route={dij|dag|dex}] [maxDepth=0.2] [assign={hun|pxa}] [maxCab=2000] [cabCapacity={2|3}] [Optional: starttime endtime]
    ```
    
    The parameters can be explained as follows:
    -   **Location:** SF|NY|SG represents the city in which you are running the simulation. SF= San Francisco, NY= New York , SG= Singapore 
    
    -   **Alpha:** Percentage Amount of extra distance that we allow the passenger to travel as compared to the shortest path from its source to its destination.
    
    -   **Route:** This parameter chooses the type of route recommendation algorithm that we run. 
    
            'dij' = Dijkstra (Shortest Path)
        
            'dag' = Use the Dynamic Programming algorithm after converting the graph into a DAG.
            
            'dex' = Use the Dynamic Programming algorithm after converting the graph into a DAG but along with back edges of                length equal to Max Depth.
    
    -   **Max Depth:** It is the maximum length of the reverse(back) edges allowed in the DAG.
    
    -   **Assign:** This represents the assignment algorithm that is used for assignment of free cabs to passengers.
    
            'hun' = Hungarian Algorithm for empty cab assignment
            
            'pxa' = Greedy Price assignment algorithm used for comparison with the VLDB paper.
    
    -   **MaxCab:** Maximum number of cabs running in the city
    
    -   **cabCapacity:** This represents the maximum number of passengers in the cab.
    
    *Optional:*
    -   **starttime:** The start time of the simulation in the day
    -   **endtime:** The end time of the simulation in the day
    
    
Thus, a sample command would look like: 
```
./a.out NY 1.2 dex 0.3 hun 4000 3 480 570
```
Here, the definitions for each variable have been mentioned in the paper.
    
    
