/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
    let i = 0;
    for (;i < arr.length - 1; i++){
        let flag = arr[i + 1]
        for (let j = i + 1; j < arr.length; j++){
            if (flag < arr[j]){
                flag = arr[j]
            }
        }
        arr[i] = flag
    }
    arr[arr.length - 1] = -1
    return arr
};