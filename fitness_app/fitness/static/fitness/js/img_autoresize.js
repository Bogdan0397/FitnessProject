<script>
    window.onload = function() {
        var img = new Image();
        img.src = '../images/lifestyle_home.png';
        img.onload = function() {
            var container = document.querySelector('.masthead.image-masthead');
            container.style.width = this.width + 'px';
            container.style.height = this.height + 'px';
        };
    };
</script>