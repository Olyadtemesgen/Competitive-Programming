func longestSubsequence(arr []int, difference int) int {
    
    dp := make(map[int]int)
    
    var answer int = 0
    
    for _, number := range arr{
        value, flag := dp[number - difference]
        
        if flag{
            dp[number] = value + 1
        }else{
            dp[number]  = 1
        }
        
        if answer < dp[number]{
            answer = dp[number]
        }
    }
    return answer
}