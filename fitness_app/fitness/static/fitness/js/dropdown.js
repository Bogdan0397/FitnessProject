document.addEventListener('DOMContentLoaded', function() {
    console.log("Dropdown script loaded");

    var dropdowns = document.querySelectorAll('.dropdown, .menu-selected');

    dropdowns.forEach(function(dropdown) {
        dropdown.addEventListener('mouseenter', function() {
            var dropdownContent = this.querySelector('.dropdown-content');
            if (dropdownContent) {
                dropdownContent.style.display = 'block';
            }
        });

        dropdown.addEventListener('mouseleave', function() {
            var dropdownContent = this.querySelector('.dropdown-content');
            if (dropdownContent) {
                dropdownContent.style.display = 'none';
            }
        });
    });
});