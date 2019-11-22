#code to implement multiprocessing in python
#this is just an example script, it can be used for any task

import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def parse(x):
    x1=x*x 
    print(x1)


list1=[3,6,8,9]
with ProcessPoolExecutor(max_workers=4) as executor:
    start = time.time()
    
    futures=[]
    for ele in list1:
        a= executor.submit(parse, ele)
        futures.append(a)
        
    results = []
    for result in as_completed(futures):
        results.append(result)
        
    end = time.time()
    print("Time Taken: {:.6f}s".format(end-start))
    
    
    
