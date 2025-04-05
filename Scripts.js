// Function to show a specific page
function showPage(pageId) {
    var pages = document.querySelectorAll('.page');
    pages.forEach(function(page) {
        page.style.display = 'none';
    });
    var pageToShow = document.getElementById(pageId);
    pageToShow.style.display = 'block';
}

// Handle the registration form submission
function handleRegistration(event) {
    event.preventDefault();  // Prevent the default form submission
    // Simulate successful registration
    alert("Registration successful! Now logging in...");
    showPage('login');  // Go to the login page after registration
}

// Handle the login form submission
function handleLogin(event) {
    event.preventDefault();  // Prevent the default form submission
    // Simulate successful login
    alert("Login successful! Now going to the cart...");
    showPage('catalog');  // Go to the cart page after login
}

// Handle cart actions (simulating proceeding to catalog)
function goToCatalogFromCart() {
    showPage('home');  // Go to the catalog page after cart
}
