// Get the dark mode checkbox
const darkModeCheckbox = document.getElementById('dark-mode-checkbox');

// Function to handle dark mode toggle
function toggleDarkMode() {
    // Toggle a class on the <body> element based on checkbox state
    document.body.classList.toggle('dark-mode', darkModeCheckbox.checked);
    
    // Save user preference to localStorage
    localStorage.setItem('darkMode', darkModeCheckbox.checked);
}

// Add event listener to the dark mode checkbox
darkModeCheckbox.addEventListener('change', toggleDarkMode);

// Check user preference from localStorage on page load
const isDarkMode = localStorage.getItem('darkMode') === 'true';
darkModeCheckbox.checked = isDarkMode; // Set checkbox state accordingly
toggleDarkMode(); // Apply dark mode based on user preference
