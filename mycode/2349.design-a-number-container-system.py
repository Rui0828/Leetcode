#
# @lc app=leetcode id=2349 lang=python3
#
# [2349] Design a Number Container System
#
import collections
# @lc code=start
class NumberContainers:

    def __init__(self):
        self.rec_in = {}
        self.rec_ni = {}
        self.rec_ni_list = collections.defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if index in self.rec_in:
            if len(self.rec_ni_list[self.rec_in[index]]) == 1:
                del self.rec_ni_list[self.rec_in[index]]
                del self.rec_ni[self.rec_in[index]]
            else:
                self.rec_ni_list[self.rec_in[index]].remove(index)
                if self.rec_ni[self.rec_in[index]] == index:
                    self.rec_ni[self.rec_in[index]] = min(self.rec_ni_list[self.rec_in[index]])


        self.rec_in[index] = number

        if number in self.rec_ni:
            self.rec_ni_list[number].append(index)
            self.rec_ni[number] = min(self.rec_ni[number], index)
        else:
            self.rec_ni[number] = index
            self.rec_ni_list[number].append(index)


    def find(self, number: int) -> int:
        if number in self.rec_ni:
            return self.rec_ni[number]
        else:
            return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @lc code=end

