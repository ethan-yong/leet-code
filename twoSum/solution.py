# Definition for singly-linked list.
import array


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current_l1 = l1
        current_l2 = l2
        output = []
        carry = 0
        remainder = 0
        index = 0

        while True:
            if current_l1 is not None or current_l2 is not None:
                value_l1 = 0
                value_l2 = 0

                if current_l1 is not None:
                    value_l1 = current_l1.val

                if current_l2 is not None:
                    value_l2 = current_l2.val

                sum_value = value_l1 + value_l2 + carry

                if sum_value >= 10:
                    # the value that would remain in the node
                    # e.g. 18%10 = 8, 8%10 = 0
                    remainder = sum_value % 10
                    # the value that is carries to the next node
                    # e.g. 28//10 = 2, 8//10 = 0
                    carry = sum_value // 10
                    output.append(ListNode(remainder, None))

                else:
                    carry = 0
                    output.append(ListNode(sum_value, None))

                if index != 0:
                    output[index-1].next = output[index] 
                
                index += 1
                
                if current_l1 is not None:
                    current_l1 = current_l1.next

                if current_l2 is not None: 
                    current_l2 = current_l2.next

            else:
                if carry != 0:
                    output.append(ListNode(carry, None))
                    output[index-1].next = output[index]

                return output


def initialise_node(array):
    output = []
    node = ListNode(array[0], None)

    for i in range(len(array)):
        if i == (len(array) - 1):
            node.next = None
        else:
            node.next = ListNode(array[i + 1], None)

        output.append(node)
        node = node.next

    return output[0]


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

l1 = [2, 4, 3]
l2 = [5, 6, 4]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

solution = Solution()
output = solution.addTwoNumbers(initialise_node(l1), initialise_node(l2))

for i in range(len(output)):
    print(output[i].val)

"""
 Testing Node Initialisation
"""

# output = initialise_node(l1)
# while output is not None:
#      print(output.val)
#      output = output.next
