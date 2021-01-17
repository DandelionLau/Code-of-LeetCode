class Solution {
public:
    bool isPalindrome(int x) {
        
        vector<int> re;
        vector<int>::iterator it;
        int temp;
        int result = 0;
        int k = 0;
        int flag = x;
        
        if(x<0)
            return false;
        
        while(x>=1){
            temp = x%10;
            x = x/10;
            re.insert(re.begin(),temp);   // insert each number at the begin of re
        }
        
        //reverse x 
         for(it=re.begin(); it!=re.end();it++) {
            result = result + (*it)*pow(10,k);
            k++;
        }
   
        if((result-flag) == 0)
            return true;
        else
            return false;
    }
};
