const fs = require('fs');
const filePath =
  process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const T = Number(input[0]);
const arr = input.slice(1);

function solution(str) {
  let answer = '';

  [...str].forEach((s) => {
    if (answer[answer.length - 1] !== s) answer += s;
  });

  return answer;
}

for (let i = 0; i < T; i++) {
  console.log(solution(arr[i]));
}
