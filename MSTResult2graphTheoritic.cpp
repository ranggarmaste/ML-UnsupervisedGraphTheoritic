#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;


int disjoint_set[32557];

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
	vector< pair<float, pair<int,int> > > v(32560);
	
	for( int i = 0; i < 32560; ++ i ){
		scanf("%d%d%f", &v[i].second.first, &v[i].second.second, &v[i].first);
	}
	
	sort( v.begin(), v.end() );
	
	
	// delete last node only because cluster of 2 

	
	// init
	for( int i = 0; i < 32000; ++ i ){
		disjoint_set[i] = i;
	}
	
	for( int i = 0; i < 32000-2; i += 2 ){
		Union(i, i + 2);
	}
	for( int i = 1; i < 32000-2; i += 2 ){
		Union(i, i + 2);
	}
	/*
	for( int i = 0; i < 32000; ++ i ){
		int a = v[i].second.first;
		int b = v[i].second.second;

		// dataset a < b
		Union(a,b);
	}*/

	for( int i = 0; i < 32000; ++ i ){
		// dataset a < b
		disjoint_set[i] = find(i);
	}
	
	set<int> s;
	
	for( int i = 0; i < 32000; ++ i ){
		s.insert( disjoint_set[i] );
	}
	
	for( auto it = s.begin(); it != s.end(); ++ it ){
		int c = *it;
		
		printf("Cluster %d\n", c );
		/*
		for( int i = 0; i < 32000; ++ i ){
			if( c == disjoint_set[i] ){
				printf("%d\n", i );
			}
		}
		*/
		
		printf("\n");
	}
	
		
	
	return 0;
}