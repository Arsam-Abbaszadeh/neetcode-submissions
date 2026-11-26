#include <iostream>

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head->next || left == right) {
            return head;
        }
        size_t count {1};
        auto dummy {ListNode{0, head}};
        auto* curr {head};

        ListNode* afterRange{}; // should be null but low key doesnt even matter
        ListNode* beforeRange{};
        auto* prev {&dummy};

        while (count <= right) {
            if (count == left) {
                beforeRange = prev;
            } else if (count == right) {
                afterRange = curr->next;
            }

            // rotate pointers
            auto next {curr->next};
            if (count >= left) {
                curr->next = prev;
            }
            prev= curr;
            curr = next;

            count++;
        }

        if (afterRange) {
            beforeRange->next->next = afterRange;
        } else {
            beforeRange->next->next = nullptr;
        }
        beforeRange->next = prev;

        return dummy.next;
    }
};