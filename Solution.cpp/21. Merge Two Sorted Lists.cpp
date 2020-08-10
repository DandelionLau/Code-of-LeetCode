/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* p;
    struct ListNode* q;
    struct ListNode* new;
    struct ListNode* temp;
    p = l1;
    q = l2;
    
    if(p == NULL)
        return q;
    else if (q == NULL)
        return p;
    
    // decisde head node
    if(p->val > q->val){
        new = q;
        q = q->next;
    }
    else{
        new = p;
        p = p->next;
    }
    
    temp = new;   
    
    //merge 
    while(p && q){
        if(p->val > q->val){
            temp->next = q;
            q = q->next;
        }else{
            temp->next = p;
            p = p->next;
        }
        temp = temp->next;
    }
    
    // if p is empty, attach q to new, else attach p to new
    if(!p)
        temp->next = q;
    else
        temp->next = p;
    return new;
    
}

