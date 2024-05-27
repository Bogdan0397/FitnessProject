document.addEventListener("DOMContentLoaded", function() {
    const menu = document.getElementById('menu');
    const menuItems = menu.getElementsByTagName('li');

    function updateMenuVisibility() {
        const windowWidth = window.innerWidth;

        for (let i = 0; i < menuItems.length; i++) {
            if (windowWidth < 800) { // Adjust this value as needed
                menuItems[i].style.display = 'none';
            } else {
                menuItems[i].style.display = 'block';
            }
        }
    }

    window.addEventListener('resize', updateMenuVisibility);
    updateMenuVisibility();
});