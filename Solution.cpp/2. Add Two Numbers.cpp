/**https://leetcode.com/problems/add-two-numbers/description/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
       
        ListNode* head = new ListNode(0);
        ListNode* p = head;
        int addc = 0;//flag for addc 
        while(l1){
            p->next = new ListNode(l1->val);
            p = p->next;
            l1 = l1->next;
        }//copy l1 to p
        ListNode* q = head;//avoid the List crash
        p = head->next;
        while((p!=NULL) && (l2!=NULL)){
            int carry1 = p->val + l2->val + addc;
            p->val = (p->val + l2->val + addc)%10;
            if(carry1<10) addc = 0;
                else addc = 1;
       
            l2 = l2->next;   
            p = p->next;
            q = q->next;
        }//end while
        while(p){//p!=NULL,l1 is the longer List
                int carry2 = p->val + addc;
                p->val = (carry2)%10;
                if(carry2<10) addc = 0;
                    else addc = 1;
                p = p->next;
                q = q->next;
            }
        while(l2){//l2!=NULL,l2 is the longe List
                    q->next = new ListNode((l2->val + addc)%10);
                    if((l2->val + addc)<10) addc = 0;
                    else addc = 1;
                    q = q->next;
                    l2 = l2->next;
                }
        if(addc) {
            q->next = new ListNode(addc);
            }   
        return head->next;
     
    }
    
};
