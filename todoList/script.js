let list = []
let test = document.getElementById("test")
let blue = []

function addToList() {
  let thing = prompt("what do you want to add to the list? ", "")
  if (thing == null || thing == "") {
    alert("no input")
  } else {
    list.push(thing)
  }
  let p = document.createElement("p");
  p.innerHTML = thing;
  test.appendChild(p);

  p.addEventListener("click", () => selected(p));
}

function selected(p) {
  if (p.style.backgroundColor == "lightblue") {
    p.style.backgroundColor = "white";
    blue.splice(blue.indexOf(p), 1)
  } else {
    p.style.backgroundColor = "lightblue";
    blue.push(p)
  }
}

function removeFromList() {
  if (blue.length == 0) {
    alert("nothing to delete")
  } else {
    for (let i = 0; i < blue.length; i++)
      test.removeChild(blue[i])
    blue = []
  }
}

function reset() {
  if (confirm("confirm reset?")) {
    list = []
    blue = []
    test.innerHTML = ""
  } else {
    alert("cancelled")
  }
}
