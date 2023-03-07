#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
#include <string>

using namespace std;
using ULL = unsigned long long;

struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    /*string convert(string s, int numRows) {
        int n = 2*numRows - 2;
        int numCols = s.length()/n;
        string ans;
    }*/
    /*vector<string> generateParenthesis(int n) {
        vector<char> stacks;
        stacks.push_back('(');
        for(int i = 1; i < n; i++)
        {

        }
    }*/
    /*void nextPermutation(vector<int>& nums) {
        vector<int> new_nums;
        int n = nums.size();
        for(int i = 0; i < n; i++)
        {
            new_nums.push_back(nums[i]);
        }
        sort(new_nums[0], new_nums[n-1]);


    }*/
    /*
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if(target <= nums[n/2] && target >= nums[0])
        {
            my_search(target, nums, 0, n/2);
        }
    }

    int my_search(int target, vector<int>& nums, int left, int right)
    {
        int n = right - left;
        if(n == 0 && nums[left] != target) return -1;
        if(target == nums[left + n/2])
        {
            return left + n/2;
        }
        else if(target < nums[left + n/2])
        {
            return my_search(target, nums, left, left + n/2);
        }
        else
        {
            return my_search(target, nums, left + n/2 + 1, right);
        }
    }*/

    //vector<string> ans;
    //vector<char> path;
    //string s;
    /*vector<string> generateParenthesis(int n)
    {
        vector<int> used(8);
        my_generate(0, n, used);
        return ans;
    }

    void my_generate(int k, int n, vector<int>& used)
    {
        if(k ==  n)
        {
            //ans.push_back(s);
            return;
        }
        for(int i = k; i < n; i++)
        {
            if(used[i] == 1) continue;
            s.push_back('(');
            path.push_back('(');
            my_generate(i+1, n, used);
            s.push_back(')');
            path.pop_back();
            used[i] = 0;
        }
    }*/

    /*int findMinMoves(vector<int>& machines) {
        int sum = 0;
        int n = machines.size();
        for(int i = 0; i < n; i++)
        {
            sum += machines[i];
        }
        int avg = sum/n;
        if(sum != avg*n) return -1;

    }*/




    int numSimilarGroups(vector<string>& strs) {
        int n = strs.size();
        int m = strs[0].length();
        
    }
};



struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if(root == NULL) return "";
        TreeNode* t;
        string ser;
        queue<TreeNode*> que;
        t = root;
        que.push(t);
        while(!que.empty())
        {
            t = que.front();
            if(t == NULL)
            {
                ser.append("null");
            }
            else
            {
                ser.append(to_string(t->val));
                que.push(t->left);
                que.push(t->right);
            }
            ser.push_back(',');
            que.pop();
        }
        ser.pop_back();
        return ser;
    }


    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int n = data.size();
        if(n == 0) return NULL;
        string ts;
        TreeNode* temp_root = new TreeNode(0);
        TreeNode* t;
        t = temp_root;
        queue<TreeNode*> que;
        que.push(t);
        int left_flag = 0;
        for(int i = 0; i < n; i++)
        {
            if(data[i] != ',')
            {
                ts.push_back(data[i]);
                if(i < n-1) continue;
            }
                t = que.front();
                if(ts == "null")
                {
                    if(left_flag)
                    {
                        t->left = NULL;
                        left_flag = 0;
                    }
                    else
                    {
                        t->right = NULL;
                        left_flag = 1;
                        que.pop();
                    }
                    ts.clear();
                }
                else
                {
                    TreeNode*p = new TreeNode(stoi(ts));
                    ts.clear();
                    //p->left = NULL;
                    //p->right = NULL;
                    if(left_flag)
                    {
                        t->left = p;
                        left_flag = 0;
                    }
                    else
                    {
                        t->right = p;
                        left_flag = 1;
                        que.pop();
                    }
                    que.push(p);
                }


        }
        return temp_root->right;
    }
};


int main()
{
    Solution S;

    //生成链表
    /*
    ListNode * head, *p;
    int m;//链表数目
    cin >> m;
    vector<ListNode*> lists;
    head = new ListNode;
    head->next = NULL;
    p = head;
    int n;//链表长度
    for(int i = 0; i < m; i++)
    {
        cin >> n;
        for(int j = 0; j < n; j++)
        {
            ListNode* temp = new ListNode;
            cin >> temp->val;
            temp->next = p->next;
            p->next = temp;
            p = p->next;
        }
        lists.push_back(head->next);
        head->next = NULL;
        p = head;
    }
    */

    Codec ser, deser;
    string data = "1,null,3";
    string ans = ser.serialize(deser.deserialize(data));
    cout << ans;






    //vector输出
    /*cout << '[';
    for(int i = 0; i < matrix.size(); i++)
    {
        cout << '[';
        for(int j = 0; j < matrix[i].size(); j++)
        {
            cout << matrix[i][j] << ' ';
        }
        cout << "]";
    }
    cout << ']';*/
    return 0;
}