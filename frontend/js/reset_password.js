let resetToken = '';

document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    resetToken = urlParams.get('token');
    
    if (resetToken) {
        document.getElementById('reset-password-form').style.display = 'block';
    } else {
        document.getElementById('invalid-token-msg').style.display = 'block';
    }
});

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

async function handleResetPasswordSubmit(event) {
    event.preventDefault();
    
    if (!resetToken) return;

    const newPassword = document.getElementById('new_password').value.trim();
    const confirmPassword = document.getElementById('confirm_password').value.trim();
    const statusAlert = document.getElementById('status-alert');
    const submitBtn = document.getElementById('submit-btn');

    statusAlert.style.display = 'none';

    if (newPassword.length < 8) {
        statusAlert.className = 'alert alert-danger';
        statusAlert.textContent = 'Password must be at least 8 characters long.';
        statusAlert.style.display = 'flex';
        return;
    }

    if (newPassword !== confirmPassword) {
        statusAlert.className = 'alert alert-danger';
        statusAlert.textContent = 'Passwords do not match.';
        statusAlert.style.display = 'flex';
        return;
    }

    submitBtn.setAttribute('disabled', 'disabled');
    submitBtn.textContent = 'Processing...';

    try {
        const response = await LEARNX_API.resetPassword(resetToken, newPassword);
        
        statusAlert.className = 'alert alert-success';
        statusAlert.textContent = response.message || 'Password reset successfully.';
        statusAlert.style.display = 'flex';
        
        // Hide form and show link to login
        document.getElementById('reset-password-form').style.display = 'none';
        
        const successMsg = document.createElement('div');
        successMsg.style.textAlign = 'center';
        successMsg.style.marginTop = '1rem';
        successMsg.innerHTML = '<a href="/auth.html" class="btn btn-primary">Go to Sign In</a>';
        document.querySelector('.auth-container').appendChild(successMsg);
        
    } catch (error) {
        statusAlert.className = 'alert alert-danger';
        statusAlert.textContent = error.message || 'Failed to reset password. The link might be expired.';
        statusAlert.style.display = 'flex';
        
        submitBtn.removeAttribute('disabled');
        submitBtn.textContent = 'Reset Password';
    }
}
