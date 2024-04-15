'use strict';

document.addEventListener('DOMContentLoaded',function (){
    function Class(){
        let arr = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']
        let choice = arr[Math.floor(Math.random()*3)+1]
        console.log(choice)
        document.getElementById('Harrypotter_class').innerHTML = `${choice}`
    };
    Class()
});