document.addEventListener('DOMContentLoaded', function (){

    const list = ["First item", "Secound item", "Third item"];


    for(let i = 0; i < list.length; ++i){
      const item = document.createElement( 'li' );
      item.setAttribute('class', 'my-list')
      item.textContent = list[i];
      document.getElementById( 'target' ).appendChild( item );
    };
});