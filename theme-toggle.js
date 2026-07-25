(function () {
    function updateIcon() {
        var btn = document.getElementById('theme-toggle');
        if (!btn) return;
        btn.textContent = document.body.classList.contains('light-theme') ? '☀️' : '🌙';
    }

    document.addEventListener('DOMContentLoaded', function () {
        if (localStorage.getItem('theme') === 'light') {
            document.body.classList.add('light-theme');
        }
        updateIcon();
        var btn = document.getElementById('theme-toggle');
        if (!btn) return;
        btn.addEventListener('click', function () {
            document.body.classList.toggle('light-theme');
            localStorage.setItem('theme', document.body.classList.contains('light-theme') ? 'light' : 'dark');
            updateIcon();
        });
    });
})();
