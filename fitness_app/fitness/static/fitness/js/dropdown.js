document.addEventListener('DOMContentLoaded', function() {
  console.log("Dropdown script loaded");

  // Используйте querySelectorAll для выбора элементов с классами 'dropdown' или 'menu-selected'
  var dropdowns = document.querySelectorAll('.dropdown, .menu-selected');

  Array.from(dropdowns).forEach(function(dropdown) {
    dropdown.addEventListener('mouseenter', function() {
      this.querySelector('.dropdown-content').style.display = 'block';
    });

    dropdown.addEventListener('mouseleave', function() {
      this.querySelector('.dropdown-content').style.display = 'none';
    });
  });
});