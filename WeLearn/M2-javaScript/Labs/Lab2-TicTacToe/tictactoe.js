const b1 = document.querySelector('#b1');
const b2 = document.querySelector('#b2');
const b3 = document.querySelector('#b3');
const b4 = document.querySelector('#b4');
const b5 = document.querySelector('#b5');
const b6 = document.querySelector('#b6');
const b7 = document.querySelector('#b7');
const b8 = document.querySelector('#b8');
const b9 = document.querySelector('#b9');

let player1 = 0;
let player2 = 1;
let currentPlayer = 0;
let color = '';

const switchPlayer= ((boxNum) => {
  if(currentPlayer == 0){
    boxNum.style.backgroundColor='red';
    currentPlayer = 1;
    console.log(currentPlayer);
  } else {
    currentPlayer = 0;
    console.log(currentPlayer);
      boxNum.style.backgroundColor='blue';
  }
});

const victoryRed = (() => {
  if(b1.style.backgroundColor ==='red' && b2.style.backgroundColor==='red' && b3.style.backgroundColor==='red') {
  console.log("you win!");
}else if(b4.style.backgroundColor ==='red' && b5.style.backgroundColor==='red' && b6.style.backgroundColor==='red'){
  console.log("you win!");
}else if (b7.style.backgroundColor ==='red' && b8.style.backgroundColor==='red' && b9.style.backgroundColor==='red') {
  console.log("you win!");
}else if (b1.style.backgroundColor ==='red' && b4.style.backgroundColor==='red' && b7.style.backgroundColor==='red') {
  console.log("you win!");
}else if (b2.style.backgroundColor ==='red' && b5.style.backgroundColor==='red' && b8.style.backgroundColor==='red') {
  console.log("you win!");
}else if (b3.style.backgroundColor ==='red' && b6.style.backgroundColor==='red' && b9.style.backgroundColor==='red') {
  console.log("you win!");
}else if (b1.style.backgroundColor ==='red' && b5.style.backgroundColor==='red' && b9.style.backgroundColor==='red') {
  console.log("you win!");
}else if (b3.style.backgroundColor ==='red' && b5.style.backgroundColor==='red' && b7.style.backgroundColor==='red') {
  console.log("you win!");
}
});
const victoryBlue = (() => {
  if(b1.style.backgroundColor ==='blue' && b2.style.backgroundColor==='blue' && b3.style.backgroundColor==='blue') {
  console.log("you win!");
}else if(b4.style.backgroundColor ==='blue' && b5.style.backgroundColor==='blue' && b6.style.backgroundColor==='blue'){
  console.log("you win!");
}else if (b7.style.backgroundColor ==='blue' && b8.style.backgroundColor==='blue' && b9.style.backgroundColor==='blue') {
  console.log("you win!");
}else if (b1.style.backgroundColor ==='blue' && b4.style.backgroundColor==='blue' && b7.style.backgroundColor==='blue') {
  console.log("you win!");
}else if (b2.style.backgroundColor ==='blue' && b5.style.backgroundColor==='blue' && b8.style.backgroundColor==='blue') {
  console.log("you win!");
}else if (b3.style.backgroundColor ==='blue' && b6.style.backgroundColor==='blue' && b9.style.backgroundColor==='blue') {
  console.log("you win!");
}else if (b1.style.backgroundColor ==='blue' && b5.style.backgroundColor==='blue' && b9.style.backgroundColor==='blue') {
  console.log("you win!");
}else if (b3.style.backgroundColor ==='blue' && b5.style.backgroundColor==='blue' && b7.style.backgroundColor==='blue') {
  console.log("you win!");
}
});





b1.addEventListener('click', () => {
  switchPlayer(b1);
  victoryRed();
  victoryBlue();
});
b2.addEventListener('click', () => {
  switchPlayer(b2);
  victoryRed();
  victoryBlue();
});
b3.addEventListener('click', () => {
  switchPlayer(b3);
  victoryRed();
  victoryBlue();

});
b4.addEventListener('click', () => {
  switchPlayer(b4);
  victoryRed();
  victoryBlue();

});
b5.addEventListener('click', () => {
  switchPlayer(b5);
  victoryRed();
  victoryBlue();

});
b6.addEventListener('click', () => {
  switchPlayer(b6);
  victoryRed();
  victoryBlue();

});
b7.addEventListener('click', () => {
  switchPlayer(b7);
  victoryRed();
  victoryBlue();

});
b8.addEventListener('click', () => {
  switchPlayer(b8);
  victoryRed();
  victoryBlue();

});
b9.addEventListener('click', () => {
  switchPlayer(b9);
  victoryRed();
  victoryBlue();

});
