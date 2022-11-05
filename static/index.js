// light mode
function lightMode(){
  // change `body`, `header`, and `logo`
  document.querySelector('body').style.backgroundColor = 'white'
  document.querySelector('body').style.color = 'black'
  document.querySelector('.header').style.backgroundColor = 'white'
  document.querySelector('.logo a').style.color = 'black'
  
  document.querySelector('.light').style.display = 'none'
  document.querySelector('.dark').style.display = 'block'
  // checking device width for responsive
  if (window.innerWidth < 701){
    // pass
    }
  else{
    // for social media links
    document.querySelector('.link_0').style.color = 'black'
    document.querySelector('.link_1').style.color = 'black'
    document.querySelector('.link_2').style.color = 'black'
    document.querySelector('.link_3').style.color = 'black'
  }
}


// dark mode
function darkMode(){
  // change `body`, `header`, and `logo`
  document.querySelector('body').style.backgroundColor = 'rgb(50, 50, 63)'
  document.querySelector('body').style.color = 'white'
  document.querySelector('.header').style.backgroundColor = 'rgb(50, 50, 63)'
  document.querySelector('.logo a').style.color = 'white'
  
  document.querySelector('.light').style.display = 'block'
  document.querySelector('.dark').style.display = 'none'
  // checking device width for responsive
  if (window.innerWidth < 701){
    // pass
    }
  else{
    // for social media links
    document.querySelector('.link_0').style.color = 'white'
    document.querySelector('.link_1').style.color = 'white'
    document.querySelector('.link_2').style.color = 'white'
    document.querySelector('.link_3').style.color = 'white'
  }
}