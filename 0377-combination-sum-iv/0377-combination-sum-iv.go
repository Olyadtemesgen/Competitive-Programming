func combinationSum4(nums []int, target int) int {
    
    list := make([]int, target + 1)
    list[0] = 1
    for i := 1; i < target + 1; i++{
        for _, val := range nums{
            
            if i - val >= 0{
                list[i] = list[i] + list[i - val]
            }
        }
    }
    return list[target]
}