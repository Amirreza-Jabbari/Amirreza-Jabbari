document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contact-form');
    const submitButton = contactForm.querySelector('button[type="submit"]');

    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();

        // Disable submit button and change text during submission
        submitButton.disabled = true;
        submitButton.textContent = 'Sending...';

        const formData = new FormData(contactForm);

        fetch('/contact/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => {
            // Check the status code directly
            return response.json().then(data => ({
                status: response.status,
                data: data
            }));
        })
        .then(({status, data}) => {
            // Success is now determined by status code
            if (status === 200) {
                submitButton.textContent = data.message || 'Message sent successfully!';
                contactForm.reset();
                setTimeout(() => {
                    submitButton.textContent = 'Send Message';
                }, 4000);
            } else {
                // Handle error scenarios
                let errorMessage = data.message || 'An error occurred';
                
                // Add detailed error handling
                if (data.errors) {
                    errorMessage += '\n';
                    for (let field in data.errors) {
                        errorMessage += `${field}: ${data.errors[field]}\n`;
                    }
                }
                
                submitButton.textContent = errorMessage;
                setTimeout(() => {
                    submitButton.textContent = 'Send Message';
                }, 2000);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        })
        .finally(() => {
            // Re-enable submit button
            // submitButton.disabled = false;
            // submitButton.textContent = 'Send Message';
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});