// Parecer Evals - Fixtures para testar candidate evaluation
package lovel_parecer

// ============================================
// Schema para Parecer
// ============================================

#ParecerTest: {
    id:       int
    prompt:   string
    expected: {
        role:       string
        level:      string
        format:     string
    }
}

testes: [
    (#ParecerTest & {
        id:     1
        prompt: "Parecer para Rafael - Desenvolvedor Go Senior - Nubank - 8 anos experiência"
        expected: {
            role:   "Go Senior"
            level:  "Senior"
            format: "parecer"
        }
    }),
    
    (#ParecerTest & {
        id:     2
        prompt: "Parecer para Ana - Tech Lead Java - Mercado Livre - 12 anos experiência"
        expected: {
            role:   "Tech Lead Java"
            level:  "Lead"
            format: "parecer"
        }
    }),
    
    (#ParecerTest & {
        id:     3
        prompt: "Parecer para Pedro - DevOps Engineer - AWS - 5 anos - Remote"
        expected: {
            role:   "DevOps"
            level:  "Sênior"
            format: "parecer"
        }
    }),
    
    (#ParecerTest & {
        id:     4
        prompt: "Parecer para Maria - Frontend React - Startup - 3 anos - CLT"
        expected: {
            role:   "Frontend"
            level:  "Pleno"
            format: "parecer"
        }
    }),
]
