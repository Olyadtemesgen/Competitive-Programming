package main

import (
    "fmt"
)

type Key struct {
    row int
    col int
}

func minimumTotal(triangle [][]int) int {
    demo := make(map[Key]int)

    return dp(triangle, demo, 0, 0)
}

func dp(triangle [][]int, demo map[Key]int, row, col int) int {
    if row == len(triangle)-1 {
        return triangle[row][col]
    }

    key := Key{row, col}
    value, flag := demo[key]
    // fmt.Println(flag);
    if flag {
        return value
    } else {
        value1 := dp(triangle, demo, row+1, col) + triangle[row][col]
        value2 := dp(triangle, demo, row+1, col+1) + triangle[row][col]
        
        if value2 <= value1 {
            demo[key] = value2
        } else {
            demo[key] = value1
        }
    }
    return demo[key]
}
