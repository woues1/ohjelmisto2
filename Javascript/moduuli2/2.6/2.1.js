'use strict';

document.addEventListener("DOMContentLoaded", function () {
    rand_num();

    function rand_num() {
        const arr = [];
        let num = 0;
        const list = document.createElement('ul');
        list.setAttribute('id', 'lista');
        document.body.appendChild(list); // Corrected this line

        while (num !== 6) {
            num = Math.floor(Math.random() * 6) + 1;
            const list_num = document.createElement('li');
            list_num.textContent = num;
            list.appendChild(list_num);
        }
    }
});
