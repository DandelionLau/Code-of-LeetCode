//https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int max = 0;                        //length of the longest substring
        int len = 0;                        //length of substring
        string sub;                         //substring
        int k = 0;                          //where to start traversing
        for(int i = 0;i<s.size();i++){
            if(sub.find(s[i])<s.size()){    //exist repeating character
                if(max<len)max = len; 
                sub.clear();
                k++;
                i = k;
                sub.push_back(s[i]);
                len = 1;

                
            } else{                          //no repeating character
               len++;
               sub.push_back(s[i]);
               
            }
            
        }//end for i
        if(max<len) max = len; 
        return max;
    }
};
