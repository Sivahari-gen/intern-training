//Theme
let btn = document.getElementById("btn");
let theme = false;
btn.addEventListener("click", ()=>{
    if(theme == false){
        document.body.style.backgroundColor = "black";
        document.body.style.color = "white";
        btn.innerText = "Dark theme"
        theme = true;
    }else{
        document.body.style.backgroundColor = "white";
        document.body.style.color = "black";
        theme = false;
        btn.innerText = "Light theme"
    }
});
//skills
let skillInput = document.getElementById("skillInput");
let skillBtn = document.getElementById("skillbtn");
let allSkill = document.getElementById("all_skill");
let skills = [];

skillBtn.addEventListener("click", ()=>{
    skills.push(skillInput.value);
    allSkill.innerHTML = "";
    skills.forEach((item)=>{
        let li = document.createElement("li");
        li.innerText = item;
        allSkill.appendChild(li);
    });
    skillInput.value = "";
});
//Qoute
let quoteBtn = document.getElementById("quote_btn");
let quote = document.getElementById("quote");
quoteBtn.addEventListener("click", () =>{
    fetch("https://dummyjson.com/quotes/1")
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        quote.innerText = data.quote + " - " + data.author;
    })
    .catch(() => {
        quote.innerText = "Unable to load quote.";
    });
});
