let article = document.getElementsByTagName('article')[0];
let lastP = article.lastElementChild;
article.removeChild(lastP);

let h2 = document.getElementsByTagName("h2")[0];
    h2.addEventListener('click', function(){
   
    h2.style.backgroundColor = 'red'

let h1 = document.getElementsByTagName("h1")[0];
let size = (
        h1.style.fontSize = `${size}px`;
        
 
        let h3 = document.getElementsByTagName("h3")[0];
        h3.addEventListener('click', function(){
            h3.style.display = 'none';
        })
        
      
        let newText = document.createTextNode('bold');
        newButton.appendChild(newText);
        newButton.classList.add('btn');
        article.appendChild(newButton);
        
        let allP = document.getElementsByTagName('p');
        newButton.addEventListener("click", boldText)
        
        function boldText(){
            for ()
                i.style.fontWeight = "bold";
        
            }
        }
        /////////////////////////2//////////////////////////////

        const getBold_items = () => {
            let arrBold = document.querySelectorAll("");
            return arrBold;
          };
          
          const highlight = () => {
            let arrBold = getBold_items();
             {
              item.style.color = "blue";
            }
          };
          
          const return_normal = () => {
            let arrBold = getBold_items();
            for (item of arrBold) {
              item.style.color = "black";
            }
          };
          
          let par = document.querySelector(".par");
          par.addEventListener("mouseover", highlight);
          par.addEventListener("mouseout", return_normal);