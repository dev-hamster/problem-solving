# 백준 with js

## 입력

```jsx
const filePath = '/dev/stdin';

// 여러 줄을 배열 형태로 입력받음
const input = require('fs')
  .readFileSync(filePath)
  .toString()
  .trim()
  .split('\n')
  .map(Number);
```
