window.addEventListener('scroll', function() {
    var footer = document.getElementById('footer');
    if (window.scrollY > 0) {
        footer.classList.add('show');
    } else {
        footer.classList.remove('show');
    }
});
