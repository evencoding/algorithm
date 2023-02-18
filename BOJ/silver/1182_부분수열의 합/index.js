const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

const [n, s] = input[0].split(' ').map(Number);
const numbers = input[1].split(' ').map(Number);

function solution(n, s, numbers) {
  let answer = 0;

  const recursiveFn = (index, sum) => {
    if (index === n) return;

    const addedCase = sum + numbers[index];
    if (addedCase === s) answer += 1;

    recursiveFn(index + 1, addedCase);
    recursiveFn(index + 1, addedCase - numbers[index]);
  };

  recursiveFn(0, 0);
  return answer;
}

console.log(solution(n, s, numbers));
