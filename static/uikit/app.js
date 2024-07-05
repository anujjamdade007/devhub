// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
  alertClose.addEventListener('click', () => 
    alertWrapper.style.display = 'none'
  )
}



const flashMessage = function () {
  const alertCloseBtn = document.querySelector('.alert__close');
  if (alertCloseBtn) {
      alertCloseBtn.addEventListener('click', (e) => {
          e.target.parentNode.style.display = 'none';
      })
  }
}

export default flashMessage;
