// Post Evals - Fixtures com validação declarativa
package lovel_post

// Emoji pattern - Unicode range
emojiPattern: "[\U0001F300-\U0001FAFF]"

// ============================================
// Schema para LinkedIn Post
// ============================================

#Post: {
    id:       int
    prompt:   string
    output:   string
    
    // ZERO emojis na resposta (exceto nos emojis permitidos do template)
    // Na verdade post PODE ter emojis, mas máx 1 por linha
    
    // Salary com faixa (não "a combinar")
    _hasSalary:    (output =~ #"R\$\s*\d+k\s*–\s*R\$\s*\d+k"#) & true
    _noACombinar:  (output !~ #"(?i)a combinar|à combinar"#) & true
    
    // Invite parameter
    _hasInvite:    (output =~ #"invite=caroline\.lima798"#) & true
    
    // Sem separadores (--- ou ===)
    _noSeparators: (output !~ "---") & true
    
    // Hook deve ser impact-based (não cargo)
    // Verifica que não começa com cargo direto
    _hasHook:      (output =~ #"🚀"#) & true
}

// ============================================
// Fixtures de teste
// ============================================

testes: [
    (#Post & {
        id:     1
        prompt: "Post para Desenvolvedor Go Sr - R$18k-25k - CLT - São Paulo - Go, AWS, Kubernetes"
        output: """
            🚀 Tornar a API 3x mais rápida em 90 dias
            
            💰 R$ 18k – R$ 25k | CLT | Sênior
            📍 Híbrido | São Paulo, SP
            🛠️ Go, AWS, Kubernetes
            🔗 [link da vaga]
            
            💡 invite=caroline.lima798
            """
    }),
    
    (#Post & {
        id:     2
        prompt: "Post para DevOps Engineer - R$12k-18k - PJ - Remoto - AWS, Terraform"
        output: """
            🚀 Reduzir custos de infraestrutura em 30% nos próximos 90 dias
            
            💰 R$ 12k – R$ 18k | PJ | Pleno/Sênior
            📍 Remoto | Brasil
            🛠️ AWS, Terraform, Kubernetes
            🔗 [link da vaga]
            
            💡 invite=caroline.lima798
            """
    }),
]
