$(document).ready(()=>{
  userSaved = []

  if (!localStorage.getItem('savedTerms')) localStorage.setItem('savedTerms', JSON.stringify(userSaved))
  // Save user choices
  $('#savefd').on('click', ()=>{
    let srchTerm = $('#searchterm').text()
    var updtFood = JSON.parse(localStorage.getItem("savedTerms"));

    if (!updtFood.includes(srchTerm)){
      updtFood.push(srchTerm)
      localStorage.setItem("savedTerms", JSON.stringify(updtFood));
      alertify.set('notifier','position', 'top-right');
      alertify.success('Food Saved Successfully');
    }else{
      alertify.set('notifier','position', 'top-right');
      alertify.warning('Food Already Saved');
    }
  })
});

$(window).on('load', ()=> {
  var updtFood = JSON.parse(localStorage.getItem("savedTerms"));

  if (updtFood.length == 0) $('#displayFood').append('No Saved Food Yet')

  updtFood.forEach((food)=>{
    $('#displayFood').append(`
    <li>
      <div class='p-2 disFoodLi d-flex justify-content-between align-items-center'>
      <a href="/results/${food}">${food}</a>
        <div class="d-flex justify-content-center align-items-center">
          <i class="fad fa-trash text-danger todele"></i>
        </div>
      </div
    </li>
    `)
  })

  todelete()
});

// sleep
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

let todelete = ()=>{
  let todeleall = [...$('.todele')]
  let disFoodLi = [...$('.disFoodLi')]
  var storedFood = JSON.parse(localStorage.getItem("savedTerms"));

  disFoodLi.forEach((item)=>{
    let txt = item.innerText
    let indx = storedFood.indexOf(txt) 

    todeleall[indx].addEventListener('click', ()=>{
      alertify.set('notifier','position', 'top-right');
      alertify.success('Food Deleted Successfully');
      sleep(100).then(() => {
        if (indx !== -1) {
          storedFood.splice(indx, 1);
        }
        localStorage.setItem("savedTerms", JSON.stringify(storedFood));
        location.reload();
      });

    })
    
  })
}
