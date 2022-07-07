/** Index JavaScript file */
function light_mode(){
	/** This function populate light mode functionalities */

	document.querySelector('body').style.backgroundColor = 'white';
	document.querySelector('body').style.color = 'black';
	document.querySelector('.header').style.backgroundColor = 'white';
	document.querySelector('.logo a').style.color = 'black';
	document.querySelector('.light').style.display = 'none';
	document.querySelector('.dark').style.display = 'block';

	// code div
	d = document.querySelectorAll('.code_div div').forEach((e) => {
		e.style.backgroundColor = 'lightgray';
	});
	document.querySelector('.code_div div').style.color = 'black';
	
	if (window.innerWidth < 701){
		// pass
	}
	else{
		// for social media links
		document.querySelector('.link_0').style.color = 'black';
		document.querySelector('.link_1').style.color = 'black';
		document.querySelector('.link_2').style.color = 'black';
		document.querySelector('.link_3').style.color = 'black';
	};
}


function dark_mode(){
	/** This function populate dark mode functionalities */

	document.querySelector('body').style.backgroundColor = 'rgb(50, 50, 63)';
	document.querySelector('body').style.color = 'white';
	document.querySelector('.header').style.backgroundColor = 'rgb(50, 50, 63)';
	document.querySelector('.logo a').style.color = 'white';
	document.querySelector('.light').style.display = 'block';
	document.querySelector('.dark').style.display = 'none';

	// code div
	d = document.querySelectorAll('.code_div div').forEach((e) => {
		e.style.backgroundColor = 'black';
	});
	document.querySelector('.code_div div').style.color = 'lightgray';
	
	if (window.innerWidth < 701){
		// pass
	}
	else{
		// for social media links
		document.querySelector('.link_0').style.color = 'white';
		document.querySelector('.link_1').style.color = 'white';
		document.querySelector('.link_2').style.color = 'white';
		document.querySelector('.link_3').style.color = 'white';
	};
}


function this_year(){
	/** This function retrieve current year we are */

	var this_year = new Date();
	document.getElementById("this_year").innerHTML = this_year.getFullYear();
}


function fdk_func(){
	/** This function display the full meaning of FDK */

	document.querySelector('.fdk').style.display = 'block';
}


function fdk_func_timeout(){
	/** This function make the full meaning of FDK to disappear */

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
