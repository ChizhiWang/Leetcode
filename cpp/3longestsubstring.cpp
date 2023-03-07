/*Given a string s, find the length of the longest 
substring
 without repeating characters.*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        if(n==0) return 0;
        int l,r;//index of window
        l = 0;
        r = 0;
        int max = 1;
        int t;//temp index
        int t_max = 1;//temp max
        while(r < n-1)
        {
            r++;
            t = r-1;
            while(t > l && s[t] != s[r])//finding repeating index
            {
                t--;
            }
            if(s[t] != s[r])//not found
            {
                t_max++;
            }
            else//found
            {
                max = t_max > max ? t_max : max;
                t_max = r-t;
                l = t+1;
            }
        }
        max = t_max > max ? t_max : max;
        return max;
    }
};

//T: O(n^2) S: O(1)
//pay attention to special cases