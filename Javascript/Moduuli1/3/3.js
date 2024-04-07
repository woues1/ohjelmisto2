'use strict';
document.addEventListener('DOMContentLoaded', function (){

    var l1 = parseInt(prompt('anna numero'))
    var l2 = parseInt(prompt('anna numero'))
    var l3 = parseInt(prompt('anna numero'))

    asd(l1, l2, l3)
    function asd(l1, l2, l3){
        let summa = l1 + l2 + l3
        let avg = summa/3

        document.getElementById('summa').innerHTML = summa
        document.getElementById('avg').innerHTML = avg
    };
});