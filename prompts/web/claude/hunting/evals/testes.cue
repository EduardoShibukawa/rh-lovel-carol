// Hunting Evals - Fixtures com validação declarativa
package lovel_hunting

// Emoji pattern - Unicode range
emojiPattern: "[\U0001F300-\U0001FAFF]"

// ============================================
// Schema para Boolean Query
// ============================================

#Hunting: {
    id:       int
    prompt:   string
    output:   string
    
    // ZERO emojis
    _noEmojis: (output !~ emojiPattern) & true
    
    // Estrutura obrigatória
    _hasICP:     (output =~ #"(?i)##\s*ICP"#) & true
    _hasSalary:  (output =~ #"(?i)##\s*Salary"#) & true
    _hasQuery:   (output =~ #"(?i)##\s*Query"#) & true
    _hasXRay:    (output =~ #"(?i)##\s*X-Ray"#) & true
    _hasNOT:     (output =~ #"(?i)##\s*NOT"#) & true
    
    // X-Ray deve ter site:linkedin.com/in
    _hasLinkedIn: (output =~ #"site:linkedin.com/in"#) & true
    
    // Salary com formato correto (R$ Xk – R$ Yk com en-dash)
    _hasSalaryFormat: (output =~ #"R\$\s*\d+k\s*–\s*R\$\s*\d+k"#) & true
    
    // NOT exclusions completas
    _hasJunior:  (output =~ #"(?i)NOT.*junior"#) & true
    _hasTrainee: (output =~ #"(?i)NOT.*trainee"#) & true
    _hasEstagio: (output =~ #"(?i)NOT.*(estagio|estágio)"#) & true
}

// ============================================
// Fixtures de teste
// ============================================

testes: [
    (#Hunting & {
        id:     1
        prompt: "Boolean para Desenvolvedor Go Sr - R$15k-22k - remoto - Go, Kubernetes, AWS"
        output: """
            ## ICP
            Senior Go developer com experiencia em microservices e cloud-native.
            
            ## Salary
            R$ 15k – R$ 22k
            
            ## Query
            ("Go" OR "Golang" OR "Go developer" OR "Gopher" OR "Go-lang" OR "Go backend" OR "Go software")
            AND (Kubernetes OR K8s OR AWS OR GCP OR Docker OR Azure OR container OR "cloud native")
            AND ("São Paulo" OR "São Paulo, SP" OR "SP" OR "Região Sudeste")
            NOT (júnior OR junior OR trainee OR estagio OR estágio OR aprendiz)
            
            ## X-Ray
            site:linkedin.com/in "Go" "Golang" "Kubernetes" "São Paulo"
            
            ## NOT
            NOT (júnior OR junior OR trainee OR estagio OR estágio OR aprendiz)
            """
    }),
]
