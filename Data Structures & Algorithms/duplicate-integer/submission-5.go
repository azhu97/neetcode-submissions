func hasDuplicate(nums []int) bool {
	// given nums []int
	// return true if any value apperas more than once
	// create a set
	// iterate through, check if in set first, then add
	// if in set, return true

	// return false at the end
	// create empty set
	s := make(map[int]struct{}, len(nums))
	for _, num := range nums {
		if _, exists := s[num]; exists {
			return true
		} else {
			s[num] = struct{}{}
		}
	}
	return false 
}