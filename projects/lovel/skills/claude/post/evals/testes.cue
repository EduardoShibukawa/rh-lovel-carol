// Post Evals - Fixtures para testar LinkedIn Post generation
package lovel_post

// ============================================
// Schema para LinkedIn Post
// ============================================

#PostTest: {
    id:       int
    prompt:   string
    expected: {
        jobTitle:  string
        salary:    string
        location:  string
        techStack: string
        contract:  string
    }
}

testes: [
    (#PostTest & {
        id:     1
        prompt: "Post para Desenvolvedor Go Sr - R$18k-25k - CLT - São Paulo - Go, AWS, Kubernetes"
        expected: {
            jobTitle:  "Go Senior"
            salary:    "R$ 18k – R$ 25k"
            location:  "São Paulo"
            techStack: "Go"
            contract:  "CLT"
        }
    }),
    
    (#PostTest & {
        id:     2
        prompt: "Post para DevOps Engineer - R$12k-18k - PJ - Remoto - AWS, Terraform"
        expected: {
            jobTitle:  "DevOps"
            salary:    "R$ 12k – R$ 18k"
            location:  "Remoto"
            techStack: "AWS"
            contract:  "PJ"
        }
    }),
    
    (#PostTest & {
        id:     3
        prompt: "Post para Tech Lead Frontend - R$20k-30k - CLT - Híbrido SP - React, TypeScript"
        expected: {
            jobTitle:  "Tech Lead Frontend"
            salary:    "R$ 20k – R$ 30k"
            location:  "São Paulo"
            techStack: "React"
            contract:  "CLT"
        }
    }),
    
    (#PostTest & {
        id:     4
        prompt: "Post para Mobile React Native - R$10k-16k - PJ - Remoto - React Native, TypeScript"
        expected: {
            jobTitle:  "Mobile"
            salary:    "R$ 10k – R$ 16k"
            location:  "Remoto"
            techStack: "React Native"
            contract:  "PJ"
        }
    }),
]
