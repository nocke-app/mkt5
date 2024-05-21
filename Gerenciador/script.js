document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Aqui você pode adicionar a lógica de autenticação
    if (username === 'admin' && password === 'admin') {
        // Redirecionar para a página admin.html
        window.location.href = 'admin.html';
    } else {
        alert('Usuário ou senha incorretos.');
    }
});

document.getElementById('create-account-link').addEventListener('click', function(event) {
    event.preventDefault();
    alert('Link para criar uma conta.');
});
