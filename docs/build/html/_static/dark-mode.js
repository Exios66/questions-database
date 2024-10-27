document.addEventListener('DOMContentLoaded', function() {
    // Create dark mode toggle button
    const toggle = document.createElement('button');
    toggle.className = 'dark-mode-toggle';
    toggle.innerHTML = '🌓';
    toggle.setAttribute('title', 'Toggle dark mode');
    document.body.appendChild(toggle);

    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
    }

    // Toggle dark mode
    toggle.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
    });
});
