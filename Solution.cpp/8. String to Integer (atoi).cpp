class Solution {
public:
    int myAtoi(string str) {
        vector<int> num;
        int flag, result,temp;
        vector<int>::iterator it;  
        flag = 0;
        result = 0;
        
        // get each number from string
        for(int i=0;i<str.length();i++){
            if(str[i]>='0' && str[i]<='9'){
                temp = str[i] - '0';
                num.insert(num.begin(),temp);
            }else if(num.empty() && flag==0 && str[i]=='+')
                flag = 1;
            else if(num.empty() && flag==0 && str[i]=='-')
                flag = 2;
            else if(!num.empty() || str[i]!=' ' || flag!=0)
                break;
        }
        
        // construct the integer
        int k = 0;

        for(it=num.begin(); it!=num.end();it++) {
            result = result + (*it)*pow(10,k);
            k++;
        }
        
        
        if(result>INT_MAX || result<=INT_MIN){
            if(flag == 2)
                return INT_MIN;
            else
                return INT_MAX;
            
        } else if(flag==2)
            result = -result;
        
        return result;
      
    }
};
