
let nav = document.getElementById("navBar");
    nav.setAttribute("id", "socialNetworkNavigation");

let newLi = document.createElement("li");
let newText = document.createTextNode("Logout");
        newLi.appendChild(newText);
let ul = document.querySelector("ul");
    ul.appendChild(newLi);

    console.log(ul.firstElementChild.textContent);
    console.log(ul.lastElementChild.textContent);



/////////////////////////////////////////////////////
let liFirstLast = document.querySelector(".list > li:last-child");
    liFirstLast.textContent = "Richard";

let ul_2 = document.querySelectorAll(".list");
    console.log(ul_2);
for (let item of ul_2) {
  let newLi2 = document.createElement("li");
  let newText2 = document.createTextNode("Hey students");
    newLi2.appendChild(newText2);
    item.appendChild(newLi2);
    console.log(item);
    }

let sarah = document.querySelectorAll(".list")[1].children[1].remove();

    for (let item of ul_2) {
  item.classList.add("student_list");
}

ul_2[0].classList.add("university", "attendance");

////////////////////////////////

let lastDiv = document.querySelectorAll("div")[2];
    lastDiv.style.backgroundColor = "lightblue";
let lastUL = lastDiv.nextElementSibling;
let john = lastUL.children[0];
    john.style.display = "none";
    lastUL.children[1].style.border = "5px Solid Black";
    document.querySelector("body").style.fontSize = "2em";
if (lastDiv.style.backgroundColor === "lightblue") {
  alert(`hello ${john.textContent} and ${lastUL.children[1].textContent}`);
    }



