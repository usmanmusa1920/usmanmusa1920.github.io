/** Base JavaScript file */
function show_menu(){
    /** Show menu bar function */

    document.querySelector('.menu').style.display = 'flex';
    document.querySelector('#menu_img').style.display = 'none';
    document.querySelector('.times').style.display = 'flex';
    document.querySelector('.times').style.fontSize = '50px';
    document.querySelector('.times').style.textDecoration = 'none';
}


function hide_menu(){
    /** Hide menu bar function */

    document.querySelector('.menu').style.display = 'none';
    document.querySelector('#menu_img').style.display = 'block';
    document.querySelector('.times').style.display = 'none';
}


function show_delete(){
    /** Function that show delete link for post */

    document.querySelector('#hidden_delete').style.display = 'block';
}


function hide_delete(){
    /** Function that hide delete link for post */
    
    document.querySelector('#hidden_delete').style.display = 'none';
}
