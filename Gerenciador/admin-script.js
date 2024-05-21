document.addEventListener('DOMContentLoaded', function() {
    const sections = {
        'taxas-link': 'taxas',
        'clientes-link': 'clientes',
        'financeiro-link': 'financeiro',
        'relatorios-link': 'relatorios',
        'acessos-link': 'acessos'
    };

    for (const [linkId, sectionId] of Object.entries(sections)) {
        document.getElementById(linkId).addEventListener('click', function(event) {
            event.preventDefault();
            showSection(sectionId);
        });
    }

    function showSection(sectionId) {
        document.querySelectorAll('.content > div').forEach(div => {
            div.classList.add('hidden');
        });
        document.getElementById(sectionId).classList.remove('hidden');

        if (sectionId === 'taxas') {
            const editButtons = document.querySelectorAll('.edit-button');
            editButtons.forEach(button => {
                button.addEventListener('click', function() {
                    const field = this.parentElement.querySelector('input[type="text"]');
                    const isDisabled = field.disabled;

                    if (isDisabled) {
                        field.disabled = false;
                        this.textContent = 'Salvar';
                    } else {
                        field.disabled = true;
                        this.textContent = 'Editar';
                        alert('Taxa salva com sucesso!');
                    }
                });
            });
        }
    }

    // Função para exibir a tela de Ajuda
    function showAjuda() {
        hideAllSections();
        document.getElementById('ajuda').classList.remove('hidden');
    }

    // Função para esconder todas as seções
    function hideAllSections() {
        document.querySelectorAll('.content > div').forEach(div => {
            div.classList.add('hidden');
        });
    }

    // Evento de clique para o link de Ajuda
    document.getElementById('ajuda-link').addEventListener('click', function() {
        showAjuda();
    });

    // Evento de clique para o link de Integrações
    document.getElementById('integracoes-link').addEventListener('click', function() {
        showIntegracoes();
    });

    // Evento de envio para o formulário de Integrações
    document.getElementById('integracoesForm').addEventListener('submit', function(event) {
        event.preventDefault();
        handleIntegracoesFormSubmission();
    });

    // Função para lidar com o envio do formulário de Integrações
    function handleIntegracoesFormSubmission() {
        const tipo = document.getElementById('integracaoTipo').value;
        const nome = document.getElementById('integracaoNome').value;
        const url = document.getElementById('integracaoURL').value;
        const descricao = document.getElementById('integracaoDescricao').value;
        const token = document.getElementById('integracaoToken').value;
        const parametros = document.getElementById('integracaoParametros').value;
        const ativa = document.getElementById('integracaoAtiva').checked;

        console.log('Tipo:', tipo);
        console.log('Nome:', nome);
        console.log('URL:', url);
        console.log('Descrição:', descricao);
        console.log('Token:', token);
        console.log('Parâmetros:', parametros);
        console.log('Ativa:', ativa);

        alert('Integração salva com sucesso!');
    }

    // Função para exibir a tela de Integrações
    function showIntegracoes() {
        hideAllSections();
        document.getElementById('integracoes').classList.remove('hidden');
    }

    // Evento de clique para o link de FAQ
    document.getElementById('faq-link').addEventListener('click', function(event) {
        event.preventDefault();
        showFaq();
    });

    // Função para exibir a tela de FAQ
    function showFaq() {
        hideAllSections();
        document.getElementById('faq').classList.remove('hidden');
    }
});
