class Solution {
public:
	int minOperations(int n) {
		int mid;
		if (n % 2 == 1) {
			mid = n / 2;
			return mid * (2 + 2 * mid) / 2;
		}
		else {
			mid = n / 2;
			return mid * (1 + 2 * mid - 1) / 2;
		}
	}
};
