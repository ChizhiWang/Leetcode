/*You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
*/

#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* p = l1;
        ListNode* q = l2;
        int v = p->val + q->val;
        int a = v/10;
        v = v%10;
        ListNode* as = new ListNode(v);
        ListNode* t = as;
        p = p->next;
        q = q->next;
        while(p && q)
        {
            v= p->val + q->val + a;
            a = v/10;
            v = v%10;
            ListNode* na = new ListNode(v);
            t->next = na;
            t = t->next;
            p = p->next;
            q = q->next;
        }
        while(p)
        {
            v = p->val + a;
            a = v/10;
            v = v%10;
            ListNode* na = new ListNode(v);
            t->next = na;
            t = t->next;
            p = p->next;
        }
        while(q)
        {
            v = q->val + a;
            a = v/10;
            v = v%10;
            ListNode* na = new ListNode(v);
            t->next = na;
            t = t->next;
            q = q->next;
        }
        if(a)
        {
            ListNode* na = new ListNode(a);
            t->next = na;
        }
        return as;
    }
};

//T:O(n) S:O(n)
// use dummyhead