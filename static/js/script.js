document.addEventListener('DOMContentLoaded', () => {
    const imageInput = document.getElementById('imageInput');
    const uploadBtn = document.getElementById('uploadBtn');
    const preview = document.getElementById('preview');
    const result = document.getElementById('result');
    const message = document.getElementById('message');

    uploadBtn.addEventListener('click', () => {
        imageInput.click();
    });

    imageInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (file) {
            // Reset previous results
            preview.style.display = 'none';
            result.style.display = 'none';
            message.textContent = 'Processing...';

            // Show preview
            preview.src = URL.createObjectURL(file);
            preview.style.display = 'block';

            // Send to backend
            const formData = new FormData();
            formData.append('image', file);

            fetch('/predict', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                result.src = data.image;
                result.style.display = 'block';
                message.textContent = `${data.result}${data.confidence ? ' (Confidence: ' + data.confidence + ')' : ''}`;
            })
            .catch(error => {
                message.textContent = 'Error processing image: ' + error.message;
                console.error('Error:', error);
            });
        }
    });
});