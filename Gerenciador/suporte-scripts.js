// suporte-scripts.js

// Função para criar e exibir um card de solicitação de suporte
function criarCardSolicitacao(solicitacao) {
    const container = document.getElementById('solicitacoes');

    const card = document.createElement('div');
    card.classList.add('card');
    card.innerHTML = `
        <h3>${solicitacao.assunto}</h3>
        <p>${solicitacao.descricao}</p>
    `;
    card.addEventListener('click', () => exibirDetalhesSolicitacao(solicitacao));
    container.appendChild(card);
}

// Função para exibir detalhes da solicitação em um modal
function exibirDetalhesSolicitacao(solicitacao) {
    // Crie um modal ou pop-up para exibir os detalhes da solicitação
    alert(`Detalhes da solicitação:\n\nAssunto: ${solicitacao.assunto}\nDescrição: ${solicitacao.descricao}`);
}

// Simulação de recebimento de solicitações (substitua isso pela lógica real)
function simularRecebimentoDeSolicitacoes() {
    // Suponha que você esteja recebendo as solicitações de algum serviço externo
    const solicitacoesRecebidas = [
        { id: 1, assunto: 'Problema no pagamento', descricao: 'Não consigo finalizar a compra de créditos.', status: 'Não Resolvido' },
        { id: 2, assunto: 'Erro ao carregar página', descricao: 'A página de compra de créditos não está carregando corretamente.', status: 'Não Resolvido' }
        // Adicione mais solicitações conforme necessário
    ];

    // Exibir as solicitações recebidas na página
    solicitacoesRecebidas.forEach(criarCardSolicitacao);
}

// Função para filtrar as solicitações com base no status
function filtrarSolicitacoes(status) {
    const container = document.getElementById('solicitacoes');
    container.innerHTML = ''; // Limpa o conteúdo atual

    // Suponha que você tenha um array de todas as solicitações
    const todasSolicitacoes = [
        { id: 1, assunto: 'Problema no pagamento', descricao: 'Não consigo finalizar a compra de créditos.', status: 'Não Resolvido' },
        { id: 2, assunto: 'Erro ao carregar página', descricao: 'A página de compra de créditos não está carregando corretamente.', status: 'Não Resolvido' }
        // Adicione mais solicitações conforme necessário
    ];

    // Filtra as solicitações com base no status
    const solicitacoesFiltradas = todasSolicitacoes.filter(solicitacao => solicitacao.status === status);

    // Exibe as solicitações filtradas
    solicitacoesFiltradas.forEach(criarCardSolicitacao);
}

// Adiciona ouvintes de eventos para os botões de filtro
document.getElementById('filtroTodos').addEventListener('click', () => filtrarSolicitacoes('Todos'));
document.getElementById('filtroResolvidos').addEventListener('click', () => filtrarSolicitacoes('Resolvido'));
document.getElementById('filtroNaoResolvidos').addEventListener('click', () => filtrarSolicitacoes('Não Resolvido'));

// Chama a função para simular o recebimento e exibição de solicitações quando a página carrega
window.onload = simularRecebimentoDeSolicitacoes;
