package main

import "fmt"

func main() {
	var arrayToSort = []int{3, 5, 1, 6, 8, 2, 1, 8, 1, 6, 9, 0, 6, 7, 4}

	fmt.Print("- Array before insertion sort: ")
	fmt.Println(arrayToSort)

	// Insertion sort
	for i := 0; i < len(arrayToSort); i++ {
		current := i

		for current > 0 && arrayToSort[current] < arrayToSort[current-1] {
			arrayToSort[current], arrayToSort[current-1] = arrayToSort[current-1], arrayToSort[current]
			current--
		}
	}

	fmt.Print("- Array after insertion sort: ")
	fmt.Println(arrayToSort)
}
