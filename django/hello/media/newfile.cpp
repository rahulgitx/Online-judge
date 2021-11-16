#include <bits/stdc++.h>
using namespace std;

long long maxsubarraysum(int arr[], int n){
	int currmax = 0, maxans = arr[0];
	for(int i=0; i<n; i++){
		maxans = arr[i];
	}
	return maxans;
}

int main(){
	int n;
	cin >> n;
	int arr[n];
	for(int i=0; i<n; i++){
		cin >> arr[i];
	}
	cout << maxsubarraysum(arr,n);
}
