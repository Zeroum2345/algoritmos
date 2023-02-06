#include <iostream>
using namespace std;

int main()
{
    int arrayToSort[] = {3,5,1,6,8,2,1,8,1,6,9,0,6,7,4};
	int length = sizeof(arrayToSort) / sizeof(int);

    // Print values
	cout << "- Array before bubble sort: { ";
	for(int i : arrayToSort){
		cout << i << " ";
	}
	cout << "}" << endl;
	// ------------------------------------

    // Bubble sort
    for(int i = 0; i < length; i++){
        for(int j = 0; j < length; j++){
            if(j != 0 && arrayToSort[j] < arrayToSort[j-1]){
                int temp = arrayToSort[j];
                arrayToSort[j] = arrayToSort[j-1];
                arrayToSort[j-1] = temp;
            }
        }
    }
    // ------------------------------------

    // Print result
	cout << "- Array after bubble sort: { ";
	for(int i : arrayToSort){
		cout << i << " ";
	}
	cout << "}";

    return 0;
}
