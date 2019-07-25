/*const names = ["Alice", "bob", "charlie", "deborah", "evan"];

for(let i = 0; i < names.length; i++){
  console.log(names[i]);
}console.log("You've finished the array");

names.forEach((name)=>{
  console.log(name);
});console.log("You've finished the array");


const books = ["Pluto", "The Alchemist", "One Piece", "Narnia","Harry Potter"];
for(let j = 0; j<books.length;j++) {
  console.log("I really love "+books[j]);
}

books.forEach((book)=>{
  console.log("I really love "+ book);
});

let sum =0;
let numbers =[1,2,3,4,5,6,7,8,9,10];

const findTotal = ((item) => {
  sum = sum + item;
});
/*calling it -->numbers.forEach(findTotal) then sum */

const buttons = document.querySelectorAll("button");
const box = document.querySelector("#box");

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    const color = button.innerHTML;
    box.style.background=color;
  });
});
