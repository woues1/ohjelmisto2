'use strict';

document.addEventListener('DOMContentLoaded', function (){

    const names = ['John', 'Paul', 'Jones'];

    const target = document.getElementById('target')


    for(let i = 0; i < names.length; ++i){
    target.innerHTML += '<li>'+names[i]+'</li>';
    };

});