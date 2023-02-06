#include <iostream>
using namespace std;


int main()
{
	int arrayToSort[] = {3,5,1,6,8,2,1,8,1,6,9,0,6,7,4};
	int length = sizeof(arrayToSort) / sizeof(int);

	// Print values
	cout << "- Array before selection sort: { ";
	for(int i : arrayToSort){
		cout << i << " ";
	}
	cout << "}" << endl;
	// ------------------------------------

	// Selection sort
	for(int i = 0; i < length; i++){
		int lowerNumberIndex = i;

		// Find lower number
		for(int j = i; j < length; j++){
			if(arrayToSort[j] < arrayToSort[lowerNumberIndex]){
				lowerNumberIndex = j;
			}
		}

		// Change values
		int temp = arrayToSort[i];
		arrayToSort[i] = arrayToSort[lowerNumberIndex];
		arrayToSort[lowerNumberIndex] = temp;
	}
	// ------------------------------------

	// Print result
	cout << "- Array after selection sort: { ";
	for(int i : arrayToSort){
		cout << i << " ";
	}
	cout << "}";

	return 0;
}