class Node:
    def __init__(self, val, next = None, isStartAndBack = True):
        self.val = val
        self.next = next
        self.isStartAndBack = isStartAndBack

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # val
        max_num = 10 ** 9
        min_num = -10 ** 9
        sequences = {}
        for num in nums:
            to_merge = False
                # check if can be added to end of sequence
            new_node = Node(num)
            if num > min_num and num - 1 in sequences:
                sequences[num - 1].next = new_node
                if not sequences[num - 1].isStartAndBack:
                    sequences[num - 1].isStartAndBack = False
                    del sequences[num - 1]
                                            
                to_merge = True
            sequences[num] = new_node
            if num < max_num and num + 1 in sequences:
                new_node.next = sequences [num + 1]
                if not to_merge:
                    sequences[num] = new_node
                if not sequences[num + 1].isStartAndBack:
                    sequences[num + 1].isStartAndBack = False
                    del sequences[num + 1]

        longest_seq = 0
        curr_seq = 0
        for seq in sequences.values():
            while seq != None:
                curr_seq += 1
                seq = seq.next
            longest_seq = max(longest_seq, curr_seq)
            curr_seq = 0
        
        return longest_seq