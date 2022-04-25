// console.log("Connected")
// var data={{inp}}
// console.log(data)
// data.style.color="blue"



// function keyword(){
//     console.log("input")
//     {{inp}}
//     var input=document.getElementById("word").value
// console.log("user value is",input)
    
// }



async function copy(text, id) {  
    // test(); 
    var textArea = document.createElement("textarea");   
    textArea.innerText = text; 
    console.log(text) 
    document.body.appendChild(textArea);    
    textArea.select();    
    textArea.setSelectionRange(0, 99999);    
    navigator.clipboard.writeText(textArea.value);
    var tooltip = document.getElementById(id);    
    tooltip.innerHTML = "Copied";  
    textArea.remove(); 
    await sleep(1500);
    outFunc(id);
  }

  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

  function outFunc(id) {    
    var tooltip = document.getElementById(id);    
    tooltip.innerHTML = "Copy";  
}






