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
            var theme = document.body.classList.contains('light-theme') ? 'light' : 'dark';
            localStorage.setItem('theme', theme);
            updateIcon();
            window.dispatchEvent(new CustomEvent('themechange', { detail: { theme: theme } }));
        });

        var navToggle = document.querySelector('.nav-toggle');
        var nav = document.querySelector('.topbar nav');
        if (navToggle && nav) {
            navToggle.addEventListener('click', function () {
                var isOpen = nav.classList.toggle('open');
                navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
            });
            nav.querySelectorAll('a').forEach(function (link) {
                link.addEventListener('click', function () {
                    nav.classList.remove('open');
                    navToggle.setAttribute('aria-expanded', 'false');
                });
            });
        }
    });
})();
