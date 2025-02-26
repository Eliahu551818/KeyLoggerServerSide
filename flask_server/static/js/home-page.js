function loadPage(page) {
    document.getElementById('contentFrame').src = page;
}

function loadUsers() {
    fetch('https://keyloggerserverside.onrender.com/users/list_of_users')
        .then(response => response.json())
        .then(users => {
            const select = document.getElementById('userSelect');
            // Clear existing options except the first one
            while (select.options.length > 1) {
                select.remove(1);
            }
            
            // Add new options from the received users
            users.users.forEach(user => {
                const option = document.createElement('option');
                option.value = user._id;
                option.text = `${user.nickname} (${user.mac_address})`;
                select.appendChild(option);
            });

        // Optionally, select the first user by default
        if (users.length > 0) {
            select.selectedIndex = 1;
        }
        })
        .catch(error => {
            console.error('Error fetching users:', error);
            alert('Failed to load users');
        });
}

let currentSelectedId = ''; // Store the selected ID
function monitorSelectedId() {
    const selectElement = document.getElementById('userSelect');
    const iframe = document.getElementById('contentFrame'); // Define iframe here
    currentSelectedId = selectElement.value; // Initial value
    
    // Set initial iframe src based on current value
    if (currentSelectedId) {
        iframe.src = updateIframeUrl(iframe.src, currentSelectedId);
    } else {
        iframe.src = updateIframeUrl(iframe.src); // Default ID
    }

    selectElement.addEventListener('change', () => {
        currentSelectedId = selectElement.value; // Update on change
        if (currentSelectedId) {
            iframe.src = updateIframeUrl(iframe.src, currentSelectedId); // Update iframe with new ID
        } else {
            iframe.src = updateIframeUrl(iframe.src); // Default ID if empty
        }
    });
}

// Helper function to update the id parameter in the iframe URL
function updateIframeUrl(currentSrc, newId = null) {
    const url = new URL(currentSrc, window.location.origin); // Parse the current src
    if (newId) {
        url.searchParams.set('id', newId); // Set or update the 'id' parameter
    }
    return url.toString(); // Return the updated URL
}

function loadPage(endpoint) {
    const url = currentSelectedId ? `${endpoint}?id=${currentSelectedId}` : endpoint;
    document.getElementById('contentFrame').src = url;
}

document.addEventListener('DOMContentLoaded', () => {
    monitorSelectedId();
});
// Load users when the page loads
window.onload = function() {
    loadUsers();
};

function logoutUser() {
    fetch('/logout', {
        method: 'POST', // Specify POST method
        headers: {
            'Content-Type': 'application/json', // Optional, depending on Flask setup
            // Include CSRF token if required (see Flask-WTF or similar)
        },
        credentials: 'include' // Include cookies (like session) if needed
    })
    .then(response => response.json()) // Parse the JSON response (True from Flask)
    .then(data => {
        if (data === true) { // Check if response is True
            window.location.href = '/login'; // Redirect to /login
        } else {
            console.error('Logout failed:', data); // Log error if False or unexpected
        }
    })
    .catch(error => {
        console.error('Error during logout:', error); // Handle fetch errors
    });
}