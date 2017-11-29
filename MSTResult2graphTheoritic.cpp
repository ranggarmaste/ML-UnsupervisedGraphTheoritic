#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;


int disjoint_set[40000];

int find(int i){
	if( disjoint_set[i] == i )
		return i;
	else // find while update
		return disjoint_set[i] = find( disjoint_set[i] );
}

int Union(int i, int k){
	int x = find( i );
	int y = find( k );
	if( x < y )
		disjoint_set[x] = y;
	else
		disjoint_set[y] = x;
}

int main(){
	int V, K; // jumlah vertices sama cluster
	scanf("%d%d", &V, &K);

	vector< pair<float, pair<int,int> > > v(V);
	
	for( int i = 0; i < V; ++ i ){
		scanf("%d%d%f", &v[i].second.first, &v[i].second.second, &v[i].first);
	}
	
	sort( v.begin(), v.end() ); // sort smallest to biggest distance
	
	// init
	for( int i = 0; i < V-K+1; ++ i ){
		disjoint_set[i] = i;
	}
	
	for( int i = 0; i < V-K+1; ++ i ){
		int a = v[i].second.first;
		int b = v[i].second.second;

		// dataset a < b
		Union(a,b);
	}

	for( int i = 0; i < V-K+1; ++ i ){
		// dataset a < b
		disjoint_set[i] = find(i);
	}
	
	set<int> s;
	
	for( int i = 0; i < V-K+1; ++ i ){
		s.insert( disjoint_set[i] );
	}
	
	for( auto it = s.begin(); it != s.end(); ++ it ){
		int c = *it;
		
		printf("Cluster %d\n", c );
		for( int i = 0; i < 32000; ++ i ){
			if( c == disjoint_set[i] ){
				printf("%d\n", i );
			}
		}
		
		printf("\n");
	}
	
		
	
	return 0;
}