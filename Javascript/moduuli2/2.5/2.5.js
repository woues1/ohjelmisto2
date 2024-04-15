document.addEventListener('DOMContentLoaded', function(){

    let num = 0;
    let nums = [];

    while(true){
        num = parseInt(prompt('anna luku'));
        if(nums.includes(num)){
            break;
        };
        nums.push(num);
    };
    nums.sort();
    for(let i = 0; i < nums.length; ++i){
        console.log(nums[i]);
    };

});