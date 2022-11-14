A greedy algorithm is an approach for solving a problem by selecting the best option available at the moment. 
It does not worry whether the current best result will bring the overall optimal result. 

This algorithm may not produce the best result for all the problems. 
It is always goes for the local best choice to produce the global best result. 

1. Greedy Choice Property 
If an optimal solution to the problem can be found by choosing the best choice at each step without 
reconsidering the previous steps once chosen, the problem can be solved using a greedy approach. 
This property is called greedy choice property.

2. Optimal Substructure
If the optimal overall solution to the problem corresponds to the optimal solutuion to its subproblems,
then the problem can be solved using a gredy approach. 
This is called optimal substructure. 

Greedy Algorithm 
1. Begin with the solution set is empty 
2. At each step, an item is added to the solutiuon set until a solution is reached
3. if the solution set is feasible, the current item is kept 
4. Else, the item is rejected and never considered again

# Problem
## you have to make a change of an amoun using the smallest possible number of coin: amoint $18
### Available coins are 5, 2, 1 
## Solution 
1. Create an empty set{}
2. Start with sum = 0
3. Always select the coin with the largest value until sum > 18 (Greedy choice property)
4. 