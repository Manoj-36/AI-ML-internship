from typing import List
import numpy as np


def find(n):
	arr = np.array([''] * (n + 1));
	size = 1;
	m = 1;

	while (size <= n):
		i = 0;
		while(i < m and (size + i) <= n):
			arr[size + i] = "1" + arr[size - m + i];
			i += 1;
		i = 0;
		while(i < m and (size + m + i) <= n):
			arr[size + m + i] = "3" + arr[size - m + i];
			i += 1;
		m = m << 1; # Or m = m*2;

		size = size + m;
	return arr[n] 

List1=[]
n=int(input())
for i in range(1, n+1):
    if (i != n-1):
	    find(n)
    else:
        print(find(n))


