#!/bin/bash

# Função para gerar mensagem de commit
generate_commit_message() {
    echo "🔍 Analyzing changes..."
    echo "------------------------"
    
    # Captura o diff e envia para o Cody, salvando a saída em uma variável
    COMMIT_MSG=$(git diff | cody chat --stdin -m "Write a commit message for this diff.")
    
    # Exibe a mensagem gerada
    echo -e "\n📝 Generated Commit Message:"
    echo "------------------------"
    echo "$COMMIT_MSG"
    echo "------------------------"
    
    # Pergunta se deseja usar esta mensagem para commit
    read -p "Would you like to use this message for commit? (y/n): " choice
    
    if [[ $choice == "y" || $choice == "Y" ]]; then
        # Adiciona todos os arquivos modificados ao stage
        git add .
        
        # Faz o commit com a mensagem gerada
        git commit -m "$COMMIT_MSG"
        echo "✅ Commit realizado com sucesso!"
    else
        echo "❌ Commit cancelado"
    fi
}

# Criar um alias para facilitar o uso
alias generate="generate_commit_message"

#chmod +x commit-message.sh
#source commit-message.sh
#source ~/.bashrc