'use strict';

document.addEventListener("DOMContentLoaded", function (){
    let arr = [];
    for(let i = 0; i < 5; ++i){
        arr[i] = parseInt(prompt('anna luku'))
    };

    for(let j = arr.length - 1; j >= 0; --j){
        console.log(arr[j])
    };
});