package chapter1

func InsertionSort(nums []int) []int {
	for i := 1; i < len(nums); i++ {
		key := nums[i]
		j := i - 1

		for j >= 0 && nums[j] > key {
			nums[j+1] = nums[j]
			j = j - 1
		}

		nums[j+1] = key
	}

	return nums
}
