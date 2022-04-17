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




function Copy(C){
    console.log("user value is")
        var sub = document.querySelectorAll("[id='subject']"); 
        for(var n =0; n < sub.length; n++){
            var SubjectLine=sub[n].innerText;
            // console.log(SubjectLine);
            // console.log("array based",sub[0].innerHTML);
        }   
        var cop = document.querySelectorAll("[id='copy']"); 
        for(var c =0; c < cop.length; c++){
            var text=cop[c].innerText;
            // console.log(cop);
            // console.log("array based copy----",cop[c].innerText);
        } 
        console.log("this line is before if:" ,C);
        var textArea = document.createElement("textarea");
        textArea.innerText = SubjectLine;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand("Copy");
        textArea.remove();
}

