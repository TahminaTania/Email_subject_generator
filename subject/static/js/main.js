// console.log("Connected")
// var data={{inp}}
// console.log(data)
// data.style.color="blue"
// var user = {{inp}}.style.color = "blue";


// function keyword(){
//     console.log("input")
//     {{inp}}
//     var input=document.getElementById("word").value
// console.log("user value is",input)
    
// }
function Copy(clickedBtn){
    console.log("user value is")
    var templateID = document.getElementsByClassName("sub");
    console.log(templateID)
    for (i in templateID){
        j=i.innerHTML
        console.log(j)
    }
var range = document.createRange();
range.selectNode(document.getElementById(templateID));
window.getSelection().removeAllRanges(); /* clear current selection*/
window.getSelection().addRange(range); /* to select text*/
document.execCommand("copy")
//  document.getElementById("button_copy").innerHTML="Copied";
templateID.select();
}