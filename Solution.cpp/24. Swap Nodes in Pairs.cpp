/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapPairs(struct ListNode* head){
    if (head == NULL || head->next == NULL)
        return head;
    struct ListNode* pre;       // previous node
    struct ListNode* cur;       // current node
    struct ListNode* suc;       // successive node
    pre = head;
    cur = head->next;
    
    //exchange the first two node
    head = cur;
    pre->next = head->next;
    head->next = pre;
    
    if (pre->next == NULL)
        return head;
    else{
        cur = pre->next;
        suc = cur->next;
    }

    
    while(suc){
        // exchange node pair
        pre->next = suc;
        cur->next = suc->next;
        suc->next = cur;
        
        if(cur->next){
            //reset pointer
            pre = suc->next;
            cur = pre->next;
            suc = cur->next;
        }
        else
            break;

    }
    return head;
}

