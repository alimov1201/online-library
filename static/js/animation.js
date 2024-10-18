window.addEventListener('DOMContentLoaded', (event) => {
    let textElement = document.getElementById('text');
  
    if (textElement) {
      consoleText([textElement.textContent], textElement, ['black']);
    }
  });
  
  function consoleText(words, target, colors) {
    if (!colors) colors = ['#fff'];
    let visible = true;
    let con = document.getElementById('console');
    let letterCount = 1;
    let x = 1;
    let waiting = false;
  
    target.setAttribute('style', 'color:' + colors[0]);
  
    window.setInterval(function () {
      if (letterCount === 0 && !waiting) {
        waiting = true;
        target.innerHTML = words[0].substring(0, letterCount);
        setTimeout(function () {
          let usedColor = colors.shift();
          colors.push(usedColor);
          let usedWord = words.shift();
          words.push(usedWord);
          x = 1;
          target.setAttribute('style', 'color:' + colors[0]);
          letterCount += x;
          waiting = false;
        }, 1000);
      } else if (letterCount === words[0].length + 1 && !waiting) {
        waiting = true;
        setTimeout(function () {
          x = -1;
          letterCount += x;
          waiting = false;
        }, 1000);
      } else if (!waiting) {
        target.innerHTML = words[0].substring(0, letterCount);
        letterCount += x;
      }
    }, 120);
  
    window.setInterval(function () {
      if (visible) {
        con.classList.add('hidden');
        visible = false;
      } else {
        con.classList.remove('hidden');
        visible = true;
      }
    }, 400);
  }
  