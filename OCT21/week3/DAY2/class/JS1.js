//let buttonRed = document.getElementById("red");
//let buttonBlue = document.getElementById("blue");

//function changeColor(event){
//	console.log(event)
//	let color = event.target.textContent.toLowerCase();
//	document.body.style.backgroundColor= color
//}

//buttonBlue.addEventListener("click", changeColor)

//buttonRed.addEventListener("click", changeColor)

let colors = ["blue", "yellow", "green", "pink"];

function createButton(){
    for (let i = 0; i < colors.length; i++){
        let button = document.createElement("BUTTON");
        let buttonText = document.createTextNode(colors[i]);
        button.appendChild(buttonText);
        document.body.firstElementChild.appendChild(button);
        button.addEventListener("click", changeColor);
    }
}

createButton()
function changeColor(event){
    let color = event.target.textContent.toLowerCase();
document.body.style.backgroundColor=color;
}
