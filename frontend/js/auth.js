let authMode = 'login';

function switchTab(mode) {
    authMode = mode;
    
    // Toggle active tab header styling
    document.getElementById('tab-login').classList.toggle('active', mode === 'login');
    document.getElementById('tab-register').classList.toggle('active', mode === 'register');
    
    // Show/hide email address row
    const emailGroup = document.getElementById('email-group');
    const emailInput = document.getElementById('email');
    const confirmGroup = document.getElementById('confirm-password-group');
    const confirmInput = document.getElementById('confirm_password');
    const forgotLink = document.getElementById('forgot-password-link');

    
    if (mode === 'register') {
        emailGroup.style.display = 'block';
        emailInput.setAttribute('required', 'required');
        
        confirmGroup.style.display = 'block';
        confirmInput.setAttribute('required', 'required');
        
        forgotLink.style.display = 'none';
        
        document.getElementById('submit-btn').textContent = 'Create Account';
    } else {
        emailGroup.style.display = 'none';
        emailInput.removeAttribute('required');
        
        confirmGroup.style.display = 'none';
        confirmInput.removeAttribute('required');
        
        forgotLink.style.display = 'inline-block';
        
        document.getElementById('submit-btn').textContent = 'Sign In';
    }

    // Hide any old error warnings
    document.getElementById('error-alert').style.display = 'none';
}

function togglePasswordVisibility(inputId, btnElement) {
    const input = document.getElementById(inputId);
    if (input.type === 'password') {
        input.type = 'text';
        btnElement.textContent = '🔒';
    } else {
        input.type = 'password';
        btnElement.textContent = '👁';
    }
}


async function handleAuthSubmit(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const confirmPassword = document.getElementById('confirm_password').value.trim();
    const email = document.getElementById('email').value.trim();
    const errorAlert = document.getElementById('error-alert');
    const submitBtn = document.getElementById('submit-btn');

    errorAlert.style.display = 'none';

    if (password.length < 8) {
        errorAlert.textContent = 'Password must be at least 8 characters long.';
        errorAlert.style.display = 'flex';
        return;
    }

    if (authMode === 'register' && password !== confirmPassword) {
        errorAlert.textContent = 'Passwords do not match.';
        errorAlert.style.display = 'flex';
        return;
    }

    submitBtn.setAttribute('disabled', 'disabled');
    submitBtn.textContent = 'Processing...';

    try {
        if (authMode === 'login') {
            await LEARNX_API.login(username, password);
        } else {
            await LEARNX_API.register(username, email, password);
        }
        
        // Success -> redirect to Dashboard
        window.location.href = '/dashboard.html';
    } catch (error) {
        errorAlert.textContent = error.message || 'Authentication failed. Please check your inputs.';
        errorAlert.style.display = 'flex';
        
        submitBtn.removeAttribute('disabled');
        submitBtn.textContent = authMode === 'login' ? 'Sign In' : 'Create Account';
    }
}

// If student is already logged in, redirect them to dashboard directly
document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('student_id')) {
        window.location.href = '/dashboard.html';
    }
});
