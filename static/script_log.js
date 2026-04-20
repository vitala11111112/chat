document.getElementById('registrationForm').addEventListener('submit', async function(e) {
            e.preventDefault();


            const formData = {
                name: document.getElementById('name').value,
                password: document.getElementById('password').value
            };




            try {
                const response = await fetch('http://127.0.0.1:8081/users_log', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });
                const result = response.json();
                if (result.real_acc === true) {
                    window.location.href = "chat.html";
                }


            }
            catch (error) {
                console.error('Ошибка сети или запроса:', error);
        }
        }
        );