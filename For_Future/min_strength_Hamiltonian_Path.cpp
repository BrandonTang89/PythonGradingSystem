#include <bits/stdc++.h>
using namespace std;

int n, e, u, v, w;
int adjmat[11][11];

int tsp(int c, int mask){
	if (mask == (1 << n)-1){
		 // cout << "Returning " << 0 <<endl;
		return 0; // Finished all nodes
		
	}
	int min_val = 9999;
	for (int i=0; i<n; i++){
		if ((mask & (1 << i)) != 0)continue; // If visited
		// cout << "c, i " << c << " " << i << endl;
		min_val = min(min_val, adjmat[c][i] + tsp(i, mask | (1 << i)));
	}
	return min_val;
}

		
int main(){
	
	cin >> n >> e;
	
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			adjmat[i][j] = 9999;
		}
	}
	
	
	for (int i=0;i<e;i++){
		cin >> u >> v >> w;
		u--; v--;
		adjmat[u][v] = min(adjmat[u][v],w);
		adjmat[v][u] = min(adjmat[v][u], w);
	}
	
	/*
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			cout << adjmat[i][j] << " ";
		}
		cout << "\n";
	}*/
	
	int min_val = INT_MAX;
	for (int i=0;i<n;i++){
		//scout << "i:" <<  i << endl;
		min_val = min(min_val, tsp(i, 1<<i));
	}
	
	cout << min_val << endl;
}

