package main

import "fmt"

func main() {
	var arrayToSort = []int{3, 5, 1, 6, 8, 2, 1, 8, 1, 6, 9, 0, 6, 7, 4}

	fmt.Print("- Array before bubble sort: ")
	fmt.Println(arrayToSort)

	// Bubble sort
	for i := 0; i < len(arrayToSort); i++ {
		for j := 1; j < len(arrayToSort); j++ {
			if arrayToSort[j] < arrayToSort[j-1] {
				arrayToSort[j], arrayToSort[j-1] = arrayToSort[j-1], arrayToSort[j]
			}
		}
	}

	fmt.Print("- Array after bubble sort: ")
	fmt.Println(arrayToSort)
}
