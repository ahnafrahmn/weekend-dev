class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result_stack = []
        sorted_list = list(zip(position, speed))
        sorted_list.sort(reverse=True)
        result_stack.append((target - sorted_list[0][0])/sorted_list[0][1])
        for i in range(1, len(sorted_list)):
            temp = (target - sorted_list[i][0])/sorted_list[i][1]
            if temp > result_stack[-1]: result_stack.append(temp)
        return len(result_stack)