function print_result(){
    console.log([...document.querySelectorAll(".input")].map(function(e) {return e.value}));
    let inputs = [...document.querySelectorAll(".input")].map(function(v){return parseInt(v.value);});
    let target = parseInt(document.querySelector(".target").value);
    document.querySelector("p").innerHTML = solve(target,inputs,[]).join("<br />");
}
