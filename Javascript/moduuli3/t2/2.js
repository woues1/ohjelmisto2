document.addEventListener('DOMContentLoaded', function (){

    const list = ["First item", "Secound item", "Third item"];

    const target = document.getElementById('target')


    for(let i = 0; i < list.length; ++i){
      const item = document.createElement( 'li' );
      item.setAttribute('class', 'my-list')
      item.textContent = list[i];
      target.appendChild( item );
    };

    target.getElementsByTagName('li')[1].setAttribute('class','my-item')
});