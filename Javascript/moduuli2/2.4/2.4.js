'use strict';
document.addEventListener('DOMContentLoaded', function(){

    let nums = []
    let num;
    do{
        num = parseInt(prompt('Anna luku. ( 0 <- lopettaa )'));
        nums.push(num);
    }while(num !== 0);

    nums.sort()

    for(let i = nums.length -1; i > 0 ; i--){
        console.log(nums[i]);
    };

});