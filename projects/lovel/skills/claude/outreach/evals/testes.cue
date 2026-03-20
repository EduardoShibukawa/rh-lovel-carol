// Outreach Evals - Fixtures com validação declarativa
package lovel_outreach

// ============================================
// M1 Schema
// ============================================

#M1: {
    id:       int
    prompt:   string
    output:   string
    
    // Constraints (forçados a true)
    _len:    (len(output) <= 200) & true
    _carol:  (output =~ "Carol|Lovel") & true
    _formal: (output !~ #"(\bPrezado\b|\bCaro\b)"#) & true
    _combin: (output !~ "a combinar") & true
    _dash:   (output !~ "---") & true
}

testesM1: [
    (#M1 & {
        id:     1
        prompt: "M1 para Luffy - Java Sr"
        output: "Oi Luffy! Sou a Carol da Lovel. Vi seu perfil e acredito que possa interessar: Java Backend Sr R$10k-13k. Está aberto a oportunidades?"
    }),
    
    (#M1 & {
        id:     2
        prompt: "M1 para Zoro - Python Sr"
        output: "Oi Zoro! Sou Carol da Lovel. Vi seu perfil e acredito que possa interessar: Python Senior R$15k-19k remoto. Top?"
    }),
    
    (#M1 & {
        id:     3
        prompt: "M1 para Sanji - Tech Lead"
        output: "Oi Sanji! Sou Carol da Lovel. Vi seu perfil e acredito que possa interessar: Tech Lead Java. Top?"
    }),
]

// ============================================
// M2 Schema
// ============================================

#M2: {
    id:          int
    prompt:      string
    salaryRange: string
    output:      string
    
    _len:     (len(output) <= 500) & true
    _salary:  (output =~ #"R\$"#) & true
    _invite:  (output =~ "invite=") & true
    _combin:  (output !~ "a combinar") & true
    _dash:    (output !~ "---") & true
}

testesM2: [
    (#M2 & {
        id:          1
        prompt:      "M2 para Luffy - Java Sr"
        salaryRange: "R$ 10k – R$ 13k"
        output:      "Perfeito! Mais detalhes:\n\nEmpresa: Nubank\nCargo: Backend Engineer Sr\nStack: Java, Spring Boot, AWS\nModelo: Híbrido | São Paulo\nSalary: R$ 10k – R$ 13k | CLT\n\nFaz sentido? 🔗 https://lovel.com.br/vaga?invite=caroline.lima798"
    }),
]

// ============================================
// Follow-up Schema
// ============================================

#Followup: {
    id:     int
    prompt: string
    day:    4 | 7
    output: string
    
    _len:    (len(output) <= 300) & true
    _formal: (output !~ #"(\bPrezado\b|\bCaro\b)"#) & true
    _combin: (output !~ "a combinar") & true
}

testesFollowup: [
    (#Followup & {
        id:     1
        prompt: "Follow-up Day 4"
        day:    4
        output: "Oi Luffy! Passando pra ver se viu 😊"
    }),
    
    (#Followup & {
        id:     2
        prompt: "Follow-up Day 7"
        day:    7
        output: "Oi Nami! Entendo se não for o momento. Boa sorte!"
    }),
]
