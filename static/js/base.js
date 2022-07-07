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


function val_required_fields(which_dm){
	/**
	 * Function that validate user inputs, for direct message page and that of pop-up in menu.
	 * 
	 * `which_dm` it will be either `dm_page` or `dm_pop`
	*/
	
	if (which_dm == 'dm_page'){
		val_name = document.querySelector('#dm_page_js_val_id_full_name');
		val_mail = document.querySelector('#dm_page_js_val_id_email');
		val_text = document.querySelector('#dm_page_js_val_id_text_body');
	}
	else if (which_dm == 'dm_pop'){
		val_name = document.querySelector('#dm_pop_js_val_id_full_name');
		val_mail = document.querySelector('#dm_pop_js_val_id_email');
		val_text = document.querySelector('#dm_pop_js_val_id_text_body');
	};

	unwanted_value = [];
	fields_values = [];

	fields_values.push(val_name.value);
	fields_values.push(val_mail.value);
	fields_values.push(val_text.value);

	function restrict_window_click(){
		/** A request validator function, that will restrict user from clicking anywhere. */

		document.querySelector('.dew').style.display = 'flex';
		document.querySelector('.container').style.position = 'fixed';
	};

	// global search of email validation, which validate email that doesn't start with white-space or @ symbol (one or more character), plus @ symbol, plus not white-space or @ symbol (one or more character), plus . character, plus white-space or @ symbol (one or more character)
	reg = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

	for (i = 0; i < fields_values.length; i++){
		eval = fields_values[i];

		if (eval == ''){
			if (val_name.value == eval){
				val_name.style.border = 'solid red 3px';
			};

			if (val_mail.value == eval){
				if (val_mail.value.match(reg)){
					// pass
				}
				else{
					val_mail.style.border = 'solid red 3px';
				};
			};

			if (val_text.value == eval){
				val_text.style.border = 'solid red 3px';
			};

			unwanted_value.push('bad');
		}
		else{
			if (val_name.value == eval){
				val_name.style.border = 'none';
			};

			if (val_mail.value == eval){
				if (val_mail.value.match(reg)){
					val_mail.style.border = 'none';
				}
				else{
					// pass
				};
			};

			if (val_text.value == eval){
				val_text.style.border = 'none';
			};
		};
	};

	// checking if unwanted value exist in our `unwanted_value` list.
	if (unwanted_value.includes('bad')){
		// pass
	}
	else{
		// if all validation pass, this will follow 🚀 ✅ that is good.
		restrict_window_click();
	};
}
