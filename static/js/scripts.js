function setRandomNumber() {
	var cells = document.querySelectorAll("td[id^='cell']"); // id属性がcellで始まるすべてのtd要素を取得

	for (var i = 0; i < cells.length; i++) {
	  var randomNumber = Math.floor(Math.random() * 200) + 1; // 1から200までのランダムな数を生成
	  cells[i].textContent = randomNumber; // セルにランダムな数を表示
	}
  }
