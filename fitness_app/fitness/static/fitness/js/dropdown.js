document.addEventListener('DOMContentLoaded', function() {
  console.log("Dropdown script loaded");

  var dropdowns = document.getElementsByClassName('dropdown');

  Array.from(dropdowns).forEach(function(dropdown) {
    dropdown.addEventListener('mouseenter', function() {
      this.querySelector('.dropdown-content').style.display = 'block';
    });

    dropdown.addEventListener('mouseleave', function() {
      this.querySelector('.dropdown-content').style.display = 'none';
    });
  });
});