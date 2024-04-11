'use strict';

document.addEventListener("DOMContentLoaded", function () {

    participants(parseInt(prompt('Anna osallistujien määrä')))
    function participants(num){
        const list = document.createElement('ol');
        list.setAttribute('id', 'lista');
        document.body.appendChild(list);
        for(let i = 0; i <= num; ++i){
            let name = prompt('Anna nimi');
            list.appendChild(name);
        };

    };
});
