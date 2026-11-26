class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head->next || left == right) {
            return head;
        }
        size_t count {1};
        auto dummy {ListNode{0, head}};
        auto* curr {head};

        ListNode* afterRange{};
        auto* prev {&dummy};

        size_t i{1};
        for (; i < left; i++) { // might need to be 0 instead bro
            prev = curr;
            curr = curr->next;
        }

        ListNode* beforeRange{prev};

        for (; i <= right; i++) {
            auto next {curr->next};
            curr->next = prev;
            prev= curr;
            curr = next;
        }

        beforeRange->next->next = curr;
        beforeRange->next = prev;
        return dummy.next;
    }
};