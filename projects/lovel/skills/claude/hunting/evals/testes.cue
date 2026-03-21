// Hunting Evals - Fixtures para testar Boolean Query generation
package lovel_hunting

// ============================================
// Schema para Boolean Query
// ============================================

#HuntingTest: {
    id:       int
    prompt:   string
    expected: {
        techStack: string
        level:     string
        salary:    string
        location:  string
    }
}

testes: [
    (#HuntingTest & {
        id:     1
        prompt: "Boolean para Desenvolvedor Go Sr - R$15k-22k - remoto - Go, Kubernetes, AWS"
        expected: {
            techStack: "Go"
            level:     "Senior"
            salary:    "R$ 15k – R$ 22k"
            location:  "Remoto"
        }
    }),
    
    (#HuntingTest & {
        id:     2
        prompt: "Boolean para Engenheiro DevOps - R$12k-18k - São Paulo - AWS, Terraform, Kubernetes"
        expected: {
            techStack: "AWS"
            level:     "Sênior"
            salary:    "R$ 12k – R$ 18k"
            location:  "São Paulo"
        }
    }),
    
    (#HuntingTest & {
        id:     3
        prompt: "Boolean para Desenvolvedor Python - R$8k-14k - remoto - Python, Django, FastAPI"
        expected: {
            techStack: "Python"
            level:     "Pleno"
            salary:    "R$ 8k – R$ 14k"
            location:  "Remoto"
        }
    }),
    
    (#HuntingTest & {
        id:     4
        prompt: "Boolean para Tech Lead Java - R$20k-30k - híbrido SP - Java, Spring, Microservices"
        expected: {
            techStack: "Java"
            level:     "Tech Lead"
            salary:    "R$ 20k – R$ 30k"
            location:  "São Paulo"
        }
    }),
    
    (#HuntingTest & {
        id:     5
        prompt: "Boolean para Mobile React Native - R$10k-16k - remoto - React Native, TypeScript"
        expected: {
            techStack: "React Native"
            level:     "Pleno/Sênior"
            salary:    "R$ 10k – R$ 16k"
            location:  "Remoto"
        }
    }),
]
