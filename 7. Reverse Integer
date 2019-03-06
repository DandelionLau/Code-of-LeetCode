class Solution {
public:
    int reverse(int x) {
        int flag;
        int temp;
        int result = 0;
        vector<int> re;
        vector<int>::iterator it;  
        
        // judege the number is plus or minus
        if(x>-2147483648 && x<2147483648){
            if(x>=0){
                flag = 0;
            }else{
                x = -x;
                flag = 1;
            }
        }else
            return 0;

        
        // get each number of integer
        while(x>=1){
            temp = x%10;
            x = x/10;
            re.insert(re.begin(),temp);   // insert each number at the begin of re
        }
        
        // construct the integer
        int k = 0;
        for(it=re.begin(); it!=re.end();it++) {
            result = result + (*it)*pow(10,k);
            k++;
        }
    
        // return the result according to flag
        cout<<result;
       
        if(result>=2147483648 || result<=-2147483648){
                return 0;
        }else if(flag)
            return -result;
        else
            return result;   
    }
};
