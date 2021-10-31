let toDoForm = document.forms[0]
toDoForm.addEventListener('submit', addTask);

let listTasks = [];


let div = document.getElementsByClassName('listTasks')[0];
let ul = document.createElement('ul');
ul.setAttribute('id','myList');
div.appendChild(ul);

 function addTask (event) {
 	event.preventDefault();
 	let inputList= event.target.elements.list
 	let listValue = inputList.value;
    

     if(listValue===""||listValue.length===0){
         alert('Enter text');
         return addTask()
     }else{
         listTasks.push(listValue);
         let newList = document.createElement('li')
         ul.appendChild(newList);
         newList.style.listStyleType='none';

         let icon = document.createElement('i');
         icon.classList.add('fas');
         icon.classList.add('fa-times-circle');
         newList.appendChild(icon);

         let newInput =document.createElement('input');
         newInput.setAttribute('type','checkbox');
         newList.appendChild(newInput);
        
         let newTask = document.createElement('label');
         let newText = document.createTextNode(listValue);
         newTask.appendChild(newText);
         newList.appendChild(newTask);

        
     }

     inputList.value="";

 }
