'use strict';

document.addEventListener('DOMContentLoaded', function () {
    let year = parseInt(prompt('Give a year'));

    if (year % 4 == 0) {
        alert(`${year} is a leap year`)
    } else if (year % 100 == 0 && year % 400 == 0) {
        alert(`${year} is a leap year`)
    } else {
        alert(`${year} is not a leap year`)
    };

});

