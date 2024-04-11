'use strict';

document.addEventListener("DOMContentLoaded", function () {
    const num = parseInt(prompt("Osallistujien määrä"));

    let participants = [];

    for (let i = 0; i < num; i++) {
        let Name = prompt("Anna nimi " + (i+1));
        participants.push(Name);
    };
    participants.sort();

    create_html(participants)
    function create_html(participants) {
        let ol = document.createElement('ol')
        document.body.appendChild(ol);

        for (let i = 0; i < participants.length; i++) {
            let list_name = document.createElement('li');
            list_name.textContent = participants[i];
            ol.appendChild(list_name);
        };
    };

});
