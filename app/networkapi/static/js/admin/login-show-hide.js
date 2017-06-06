const google = document.querySelector('form div.social-login');
const admin = document.querySelector('div.admin-access');

const toggles = Array.from(document.querySelectorAll('admin-login-toggle'));
toggles.forEach(function(toggle) {
  toggle.addEventListener( "click", function(evt) {
    [google, admin].forEach( function(e) {
      e.classList.toggle("hidden");
    });
  });
});
