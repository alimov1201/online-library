document.getElementById("burger").addEventListener("click", function() {
    const menu = document.getElementById("menu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
});

// let text = document.getElementById('text');

// consoleText(['Hello World!'], text, ['black']);

// function consoleText(words, target, colors) {
//   if (colors === undefined) colors = ['#fff'];
//   let visible = true;
//   let con = document.getElementById('console');
//   let letterCount = 1;
//   let x = 1;
//   let waiting = false;

//   // Set the initial color for the target
//   target.setAttribute('style', 'color:' + colors[0]);

//   // Animation for typing and deleting letters
//   window.setInterval(function () {
//     if (letterCount === 0 && waiting === false) {
//       waiting = true;
//       target.innerHTML = words[0].substring(0, letterCount);
//       window.setTimeout(function () {
//         let usedColor = colors.shift();
//         colors.push(usedColor);
//         let usedWord = words.shift();
//         words.push(usedWord);
//         x = 1;
//         target.setAttribute('style', 'color:' + colors[0]);
//         letterCount += x;
//         waiting = false;
//       }, 1000);
//     } else if (letterCount === words[0].length + 1 && waiting === false) {
//       waiting = true;
//       window.setTimeout(function () {
//         x = -1;
//         letterCount += x;
//         waiting = false;
//       }, 1000);
//     } else if (waiting === false) {
//       target.innerHTML = words[0].substring(0, letterCount);
//       letterCount += x;
//     }
//   }, 120);

//   // Blinking underscore animation
//   window.setInterval(function () {
//     if (visible === true) {
//       con.classList.add('hidden');
//       visible = false;
//     } else {
//       con.classList.remove('hidden');
//       visible = true;
//     }
//   }, 400);
// }
