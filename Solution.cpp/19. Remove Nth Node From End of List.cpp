/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* p = head;
    struct ListNode* q;
    int length = 0;
    int index = 0;
    int count = 0;
    while(p){
        length++;
        p = p->next;
    }
    p = head;
    index = length - n;
    while(p){
        if (index == 0){
            p = p->next;
            head = p;
            break;
        }else if(count + 1 == index){
                q = p->next;
                p->next = q->next;
                free(q);
                break;
        }
        count++;
        p = p->next;
    }
    return head;
}

