'use strict';

document.addEventListener("DOMContentLoaded", function () {

    let Dog_names = [];

    for (let i = 0; i < 6; i++) {
        let Name = prompt("Anna nimi " + (i+1));
        Dog_names.push(Name);
    };
    Dog_names.sort();

    create_html(Dog_names)
    function create_html(Dog_names) {
        let ul = document.createElement('ul');
        document.body.appendChild(ul);

        for (let i = Dog_names.length-1; i >= 0; --i) {
            let list_name = document.createElement('li');
            list_name.textContent = Dog_names[i];
            ul.appendChild(list_name);
        };
    };

});
