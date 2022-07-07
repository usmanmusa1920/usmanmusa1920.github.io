function light_mode(){
    /** Light mode functionalities */

    document.querySelector('body').style.backgroundColor = 'white';
    document.querySelector('body').style.color = 'black';
    document.querySelector('.header').style.backgroundColor = 'white';
    document.querySelector('.logo a').style.color = 'black';
    document.querySelector('.light').style.display = 'none';
    document.querySelector('.dark').style.display = 'block';
    
    // body links
    document.querySelectorAll('.links a').forEach((e) => {
        e.style.color = 'black';
    });
    
    if (window.innerWidth < 701){
        // pass
    }
    else{
        // header links
        document.querySelectorAll('.head_right a').forEach((e) => {
            e.style.color = 'black';
        });
    };
}


function dark_mode(){
    /** Dark mode functionalities */

    document.querySelector('body').style.backgroundColor = 'rgb(50, 50, 63)';
    document.querySelector('body').style.color = 'white';
    document.querySelector('.header').style.backgroundColor = 'rgb(50, 50, 63)';
    document.querySelector('.logo a').style.color = 'white';
    document.querySelector('.light').style.display = 'block';
    document.querySelector('.dark').style.display = 'none';
    
    // body links
    document.querySelectorAll('.links a').forEach((e) => {
        e.style.color = 'white';
    });
    
    if (window.innerWidth < 701){
        // pass
    }
    else{
        // header links
        document.querySelectorAll('.head_right a').forEach((e) => {
            e.style.color = 'white';
        });
    };
}


function this_year(){
    /** Retrieve current year we are */

    var this_year = new Date();
    document.getElementById('this_year').innerHTML = this_year.getFullYear();
}


function fdk_func(){
    /** Display FDK */

    document.querySelector('.fdk').style.display = 'block';
}


function fdk_func_timeout(){
    /** Disappear FDK */

    document.querySelector('.fdk').style.display = 'none';
}


function base_func(){
    /** Base function */

    var time_func = new Date();
    current_hour = time_func.getHours();

    // calling `this_year` function
    this_year();
    
    // auto light and dark mode
    if (current_hour == 7 || current_hour == 8 || current_hour == 9 || current_hour == 10 || current_hour == 11 || current_hour == 12 || current_hour == 13 || current_hour == 14 || current_hour == 15 || current_hour == 16 || current_hour == 17 || current_hour == 18){
        light_mode();
    }
    else{
        // (current_hour == 19 || current_hour == 20 || current_hour == 21 || current_hour == 22 || current_hour == 23 || current_hour == 0 || current_hour == 1 || current_hour == 2 || current_hour == 3 || current_hour == 4 || current_hour == 5 || current_hour == 6)
        dark_mode();
    };
}
