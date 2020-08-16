class Solution {
public:
	bool threeConsecutiveOdds(vector<int>& arr) {
		if (arr.size() < 3) {
			return false;
		}
		else {
			int i = 0;
			int j = i + 1;
			int k = j + 1;
			int next = 1;
			while (k < arr.size()) {
				if (isOdd(arr[i], arr[j], arr[k]) == 0) {
					return true;
				}
				else {
					if (isOdd(arr[i], arr[j], arr[k]) == 1)
						next = i + 1;
					else if (isOdd(arr[i], arr[j], arr[k]) == 2)
						next = j + 1;
					else if (isOdd(arr[i], arr[j], arr[k]) == 3)
						next = k + 1;

					i = next;
					j = i + 1;
					k = j + 1;
				}
			}
			return false;
		}
	}

	int isOdd(int num1, int num2, int num3) {
		int flag = 0; 
		if (num1 % 2 == 0) {
			flag = 1;
		}
		else if (num2 % 2 == 0) {
			flag = 2;
		}
		else if (num3 % 2 == 0) {
			flag = 3;
		}
		return flag;
	}
};
