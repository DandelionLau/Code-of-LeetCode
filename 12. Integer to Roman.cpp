class Solution {
public:
    string intToRoman(int num) {
      string s;
      vector<int> integer;
      vector<int>::iterator it;
      char r[7] = { 'I','V','X','L','C','D','M' };
      int n = 7;
      int k = 0;
      int x;
      int y;

      // get each integer
      while (num>=1) {
        integer.insert(integer.begin(), num % 10);
        num = num / 10;
        k++;
      }

      // transfer integer to roman number
      for (it = integer.begin(); it != integer.end(); it++) {
        k--;
        if ((*it)  == 1) {
          s = s + r[2 * k];
        }else{
          x = (*it) / 5;   // get the quotient
          y = (*it) % 5;   // get the remainder

          if (x == 0) {
            if (y == 4) {// integer equal to 4
              s = s + r[2 * k];
              s = s + r[2 * k + 1];
            }
            else {
              string temp;
              s = s + temp.assign(y, r[2 * k]);
            }
          }
          else {
            if (y == 4) {// integer equal to 9
              s = s + r[2 * k];
              s = s + r[2 * k + 2];
            }
            else {
              s = s + r[2 * k + 1]; // x
              string temp;
              s = s + temp.assign(y, r[2 * k]);
            }
          }
        }
      }
      return s;
    }
};
