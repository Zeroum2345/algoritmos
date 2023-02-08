package main

import "fmt"

func main() {
	var arrayToSort = []int{3, 5, 1, 6, 8, 2, 1, 8, 1, 6, 9, 0, 6, 7, 4}

	fmt.Print("- Array before selection sort: ")
	fmt.Println(arrayToSort)

	// Selection sort
	for i := 0; i < len(arrayToSort); i++ {
		lowerNumberIndex := i

		// Find lower number
		for j := i; j < len(arrayToSort); j++ {
			if arrayToSort[j] < arrayToSort[lowerNumberIndex] {
				lowerNumberIndex = j
			}
		}

		arrayToSort[i], arrayToSort[lowerNumberIndex] = arrayToSort[lowerNumberIndex], arrayToSort[i]
	}

	fmt.Print("- Array after selection sort: ")
	fmt.Println(arrayToSort)
}
