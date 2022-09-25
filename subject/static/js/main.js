// var category = document.getElementById('category').value;
// console.log("user category is",category);


var sentances=document.getElementsByClassName('subject');
var input=document.getElementById('word').value;
  for(var i = 0; i < sentances.length; i++){
    let rep = '<span style="color:black">'+input+'</span>';
    sentances[i].innerHTML = sentances[i].innerHTML.replace(input, rep);
  }

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
    await sleep(2000);
    outFunc(id);
  }

  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

  function outFunc(id) {    
    var tooltip = document.getElementById(id);    
    tooltip.innerHTML = "Copy";  
}






function loadMore(){
  console.log("loaded");

}