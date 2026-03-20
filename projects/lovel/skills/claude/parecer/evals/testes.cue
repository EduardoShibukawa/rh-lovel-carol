// Parecer Evals - Fixtures com validação declarativa
package lovel_parecer

// Emoji pattern - Unicode range
emojiPattern: "[\U0001F300-\U0001FAFF]"

// ============================================
// Schema para Parecer
// ============================================

#Parecer: {
    id:       int
    prompt:   string
    output:   string
    
    // Estrutura obrigatória
    _hasResumo:        (output =~ #"(?i)resumo"#) & true
    _hasExperiencia:   (output =~ #"(?i)experi(ência|encia)"#) & true
    _hasStack:         (output =~ #"(?i)stack"#) & true
    _hasPontosFortes:  (output =~ #"(?i)pontos fortes"#) & true
    _hasPontosAtencao: (output =~ #"(?i)pontos de aten"#) & true
    _hasRecomendacao:  (output =~ #"(?i)recomenda"#) & true
    _hasVersaoCurta:   (output =~ #"(?i)vers[aã]o curta"#) & true
    
    // ZERO emojis
    _noEmojis: (output !~ emojiPattern) & true
    
    // PT-BR básico (palavras comuns em inglês)
    _noRandomEN: (output !~ #"\b(the|and|or|for|with|from|this|that)\b"#) & true
    
    // Não aceita tyops comuns
    _noTypos: (output !~ #"expectativas"#) & true
}

// ============================================
// Fixtures de teste
// ============================================

testes: [
    (#Parecer & {
        id:     1
        prompt: "Parecer para Luffy - Java Sr"
        output: """
            Parecer do Hunter | Luffy | Backend Engineer Sr
            
            Resumo do perfil
            Luffy é desenvolvedor Java Senior com mais de 10 anos de experiência em desenvolvimento
            de sistemas corporativos. Atua com foco em Spring Boot e arquitetura de microsserviços.
            Atualmente na Straw Hat Pirates, empresa do setor de tecnologia.
            
            Experiência relevante
            Straw Hat Pirates (2022 – atual)
            Backend Engineer Sr responsável por sistemas de navegação e logística. Atua com Java,
            Spring Boot, PostgreSQL e microsserviços em ambiente de alta disponibilidade.
            
            Stack / Tecnologias
            Backend: Java, Spring Boot, Kotlin
            Banco: PostgreSQL, MongoDB
            Cloud: AWS
            Mensageria: Kafka, RabbitMQ
            
            Pontos fortes
            - Experiência sólida em Java e ecossistema Spring
            - Conhecimento em arquitetura de microsserviços
            - Vivência em ambientes cloud (AWS)
            
            Pontos de atenção
            - Disponibilidade para trabalho híbrido
            - Salary
            
            Avaliação do fit
            Perfil adequado para posição de Backend Engineer Sr com foco em Java.
            
            Recomendação
            [OK] Recomendo avançar para entrevista técnica, pontos a validar:
            - Projetos mais recentes com microsserviços
            - Experiência com sistemas de alta disponibilidade
            
            Versão curta: Luffy - Backend Engineer Sr - 10 anos - Java, Spring Boot, AWS - Ex-Marine.
            """
    }),
]
