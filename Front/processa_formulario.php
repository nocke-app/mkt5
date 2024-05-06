<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Verifica se todos os campos foram preenchidos
    if (isset($_POST['name']) && isset($_POST['email']) && isset($_POST['message'])) {
        // Valores do formulário
        $name = $_POST['name'];
        $email = $_POST['email'];
        $message = $_POST['message'];
        
        // Endereço de e-mail para onde enviar
        $to = "contato@mkt55.com";
        // Assunto do e-mail
        $subject = "Novo contato via formulário";
        // Mensagem formatada
        $formatted_message = "Nome: $name\n";
        $formatted_message .= "Email: $email\n";
        $formatted_message .= "Mensagem:\n$message";
        // Cabeçalhos do e-mail
        $headers = "From: $email" . "\r\n" .
                   "Reply-To: $email" . "\r\n" .
                   "X-Mailer: PHP/" . phpversion();
        
        // Envia o e-mail
        if (mail($to, $subject, $formatted_message, $headers)) {
            // Se o e-mail for enviado com sucesso, redireciona para uma página de confirmação
            header("Location: obrigado.html");
            exit();
        } else {
            // Se houver um erro ao enviar o e-mail, redireciona para uma página de erro
            header("Location: erro.html");
            exit();
        }
    }
}
?>
