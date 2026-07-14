class Solution {
    public int search(int[] nums, int target) {
        return binSearchHelper(0, (nums.length - 1), nums, target);
    }
    public int binSearchHelper(int low, int high, int[] nums, int target) {
        int mid = low + ((high - low) / 2);
        if (low > high) {
            return -1;
        }
        if (nums[mid] == target) {
            return mid;
        }
        if (nums[mid] > target) {
            return binSearchHelper(low, (mid - 1), nums, target);
        } else {
            return binSearchHelper((mid + 1), high, nums, target);
        }
    }
}
