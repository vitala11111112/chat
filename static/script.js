document.getElementById('registrationForm').addEventListener('submit', async function(e) {
            e.preventDefault(); 
            
           
            const formData = {
                name: document.getElementById('name').value,
                password: document.getElementById('password').value
            };
            
            
            
            
            try {
                const response = await fetch('http://127.0.0.1:8080/users', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData) 
                });
                
                
            }
            catch (error) {
                console.error('Ошибка сети или запроса:', error);
        }
        }
        );