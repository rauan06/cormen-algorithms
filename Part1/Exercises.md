# cormen-algorithms
 
 Cormen ALgorithms:
 
 
 
 Part 1.1
 
 Ex. 1.1
 
 1 - 2gis and taxi require to find a shortest path from point A to point B. Internet signals and delivery routes require this feature as well. In library, it is really challenging to find a book if the books aren't sorted well enough. In supermarkets
 
 2 - Memory usage
 
 3 - Hash tables:
 
 Strengths = [fast search O(1), fast input and removal]
 
 Weaknesses = [No random access, Unordered, degrade if they go through a large number of collisions]
 
 4 - Similarity = [both try rto find th shortest path]
 
     Difference = [Sales man Person has many points and we dont know where to start, in shortest path we know our start and destination]
 
 5 - Rocket launching and building, physics. Statistics, where scientists need to guess the outcome or create and conclude a resuslt
 
 6 - In 2gis, I just add two points and program shows the shortest path. Tesla cars have no idea about the inputs before going down the road, it is fully build on online algorithms.
 
 
 
 
 
 Part 1.2
 
 Ex 1.2
 
 1 - CS2 needs algorithms at the application level, CPU building companies focucs their attention on algorithms. In CS2 algorithms are must have in animation, game engine and shooting. In CPU, everything is about algorithms and getting input values then transforming it into the ouput.
 
 2 - 	Inser. vs Merge
 
 	8n^2 < 64n lg(n)
 
     	8n < lg(n)
 
 	8 < lg(n)/n
 
 	16: 8 < 4/16=1/4
 
 	8: 8 < 3/8
 
 	2: 8 < 1/2
 
 	1: 8 < 0
 
 	32: 8 < 8/32=1/4
 
 	~350
 
 3 - 	alg1 vs alg2
 
 	100n^2 < 2^n
 
 	N = 14 
 
 Problems \
 1 - 1 \
 ![alt text](image.png) 

 Ex 2.1
 1 - Insertion sort
```python
arr = [31, 41, 59, 26, 41, 58]
for i in range(1, len(arr)):
    key = arr[i]
    # Insert arr[i] into the sorted subarray arr[1:i - 1]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print(arr)
```
 Result
```python
[26, 31, 41, 41, 58, 59]
```

2 - Sum Array
```python
summ = 0  
for i in range(len(arr)):
    summ += arr[i]

print(summ)
```
4 - Linear search
```python
def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
```




 ![alt text](image.png) 





 