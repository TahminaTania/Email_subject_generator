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





num=0;
numB=3

function loadMore(){
  console.log("loaded");
    if((num<sub.length) && (num+3<sub.length)){
    numB=numB+3
    num=num+3
    print("firstone")
    }
    else if(num==sub.length){
    num=3
    numB=0
    print("2one")
    }
    else if(num+3>sub.length){
    numB=sub.length-3
    num=sub.length
    print("3one")
    }
    else{
    num=num+3
    numB=numB+3
  }


}