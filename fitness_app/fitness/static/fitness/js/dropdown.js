// dropdown.js
// This script will allow dropdown menus to function on hover

document.addEventListener('DOMContentLoaded', function() {
  var dropdowns = document.querySelectorAll('.dropdown');

  dropdowns.forEach(function(dropdown) {
    dropdown.addEventListener('mouseenter', function() {
      this.querySelector('.dropdown-content').style.display = 'block';
    });

    dropdown.addEventListener('mouseleave', function() {
      this.querySelector('.dropdown-content').style.display = 'none';
    });
  });
});