async function handleForgotPasswordSubmit(event) {
    event.preventDefault();
    
    const email = document.getElementById('email').value.trim();
    const statusAlert = document.getElementById('status-alert');
    const submitBtn = document.getElementById('submit-btn');

    statusAlert.style.display = 'none';
    statusAlert.className = 'alert alert-info';
    submitBtn.setAttribute('disabled', 'disabled');
    submitBtn.textContent = 'Processing...';

    try {
        const response = await LEARNX_API.forgotPassword(email);
        
        statusAlert.className = 'alert alert-success';
        statusAlert.textContent = response.message || 'If your email is registered, you will receive a password reset link shortly.';
        statusAlert.style.display = 'flex';
        
        // Disable form to prevent multiple submissions
        document.getElementById('email').setAttribute('disabled', 'disabled');
        submitBtn.textContent = 'Link Sent';
    } catch (error) {
        statusAlert.className = 'alert alert-danger';
        statusAlert.textContent = error.message || 'An error occurred. Please try again.';
        statusAlert.style.display = 'flex';
        
        submitBtn.removeAttribute('disabled');
        submitBtn.textContent = 'Send Reset Link';
    }
}
