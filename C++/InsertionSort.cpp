#include <iostream>
using namespace std;

int main()
{
    int arrayToSort[] = {3,5,1,6,8,2,1,8,1,6,9,0,6,7,4};
	int length = sizeof(arrayToSort) / sizeof(int);

    // Print values
	cout << "- Array before insertion sort: { ";
	for(int i : arrayToSort){
		cout << i << " ";
	}
	cout << "}" << endl;
	// ------------------------------------

    // Insertion sort
    for(int i = 1; i < length; i++){
        int current = i;

        // while lower than the value behind it, change values
        while (current != 0 && arrayToSort[current] < arrayToSort[current-1])
        {
            int temp = arrayToSort[current];
            arrayToSort[current] = arrayToSort[current-1];
            arrayToSort[current-1] = temp;
            current--;
        }
        
    }
	// ------------------------------------

    // Print result
	cout << "- Array after insertion sort: { ";
	for(int i : arrayToSort){
		cout << i << " ";
	}
	cout << "}";

    return 0;
}
