const google = document.querySelector('form div.social-login');
const admin = document.querySelector('div.admin-access');

const adminToggle = document.getElementById('admin-login-button');
adminToggle.addEventListener( "click", function(evt) {
  [google, admin].forEach( function(e) {
  	e.classList.toggle("hidden");
  });
});
