//Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

//The overall run time complexity should be O(log (m+n)).

#include "util.h"

class Solution {
public:
    double findMedianSortedArrays1(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        int mid = (m+n)/2;
        int k = 0;
        int i,j;
        i = 0;
        j = 0;
        int v1, v2;
        int v_mid_p, v_mid;//mid value
        while((i < m || j < n) && k <= mid)
        {
            v1 = i<m ? nums1[i] : INT_MAX;
            v2 = j<n ? nums2[j] : INT_MAX;
            if(v1 < v2)
            {
                i++;
            }
            else
            {
                j++;
            }
            if(k == mid-1)
            {
                v_mid_p = min(v1, v2);
            }
            k++;
        }
        v_mid = min(v1,v2);
        if((m+n)%2 == 1) return v_mid;
        else return (v_mid_p+v_mid)/2.0;
    }

    double findMedianSortedArrays2(vector<int>& nums1, vector<int>& nums2)
    {
        int m = nums1.size();
        int n = nums2.size();
        if(n < m) return findMedianSortedArrays2(nums2, nums1);

        int start = 0;
        int end = m;
        while(start <= end)
        {
            int mid1 = (start + end)/2;
            int mid2 = (m+n+1)/2;
        }

    }
};

//solution 1:
//T:O(m+n) S:O(1)
//not satisfy

//solution 2: