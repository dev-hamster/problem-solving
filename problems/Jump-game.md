# Jump game

## 문제
https://leetcode.com/problems/jump-game/description/

각 배열의 인덱스에 점프할 수 있는 최대 길이가 주어진다. 마지막 인덱스까지 점프 할 수 있는지 판별해라.

## 접근
개선 전: dfs로 모든 인덱스를 확인해 점프를 해본다.

개선 후: 현재 점프할 수 있는 횟수인 `cur` 을 인덱스를 읽을때마다 최대값으로 갱신해준다.

## 코드

**개선 후**
```jsx
var canJump = function(nums) {
    if(nums.length <= 1) return true;

    let cur = nums[0];
    for(let i=1; i<nums.length; i+=1){
        if(cur===0) return false;
        cur -= 1;
        cur = Math.max(cur, nums[i])
    }
    return true;
};
```
**개선 전**
```jsx
let flag = false;
let visited = [];

var dfs = function(idx, nums) {
    if(flag) return;

    visited[idx] = true;

    for(let i=1; i<=nums[idx]; i+=1){
        let nextIdx = idx + i;
        if(visited[nextIdx]) continue;
        if(nextIdx >= nums.length-1){
            flag = true;
            break;
        }

        dfs(nextIdx, nums);
    }
}

var canJump = function(nums) {
    flag = false;
    visited = Array.from(nums, ()=>false);

    if(nums.length == 1) return true;

    dfs(0, nums)
    return flag;
};
```