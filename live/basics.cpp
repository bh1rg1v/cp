
// Basic CPP Syntax

#include <bits/stdc++.h>
using namespace std;

int main () {

    // dataType variableName[size];

    // size is optional
    // we can intialize an array partially, the rest will be initialized to 0

    int nums[5];

    int n;
    n = 10;
    int arr[n];

    int nums2[5] = {1, 2, 3, 4, 5};

    for (int i = 0; i < 5; i++) {
        cout << nums2[i] << " ";
    }

    int m, n;

    int matrix[m][n]; // 2D array

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }


    return 0;
}