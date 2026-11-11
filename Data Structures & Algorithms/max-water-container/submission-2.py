class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max= 0
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         area = (min(heights[j],heights[i]))*(j-i)
        #         if max < area:
        #             max = area
        # return max

        left = 0
        right = len(heights) - 1
        max = 0
        while(left < right):
            height = min(heights[left],heights[right])
            width = right - left
            area = height*width
            if area > max:
                max = area
            if(heights[left] < heights[right]):
                left +=1
            else:
                right = right - 1
        return max


        # area = (height[i]-hieght[y])*(i-y)