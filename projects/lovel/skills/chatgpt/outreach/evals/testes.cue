// Outreach Evals - Fixtures para testar DM personalization
package lovel_outreach

// ============================================
// Schema para Outreach (M1 + M2 + Follow-up)
// ============================================

#OutreachTest: {
    id:       int
    prompt:   string
    messageType: "M1" | "M2" | "Followup"
    expected: {
        candidateName: string
        jobTitle:      string
        salary:        string
    }
}

testes: [
    (#OutreachTest & {
        id:          1
        prompt:      "M1 para Rafael - Desenvolvedor Go Senior - R$18k-25k"
        messageType: "M1"
        expected: {
            candidateName: "Rafael"
            jobTitle:      "Go Senior"
            salary:        "R$ 18k – R$ 25k"
        }
    }),
    
    (#OutreachTest & {
        id:          2
        prompt:      "M1 para Ana - Tech Lead Java - R$25k-35k"
        messageType: "M1"
        expected: {
            candidateName: "Ana"
            jobTitle:      "Tech Lead Java"
            salary:        "R$ 25k – R$ 35k"
        }
    }),
    
    (#OutreachTest & {
        id:          3
        prompt:      "M2 para Rafael - DevGo Sr - Nubank - R$18k-25k - CLT"
        messageType: "M2"
        expected: {
            candidateName: "Rafael"
            jobTitle:      "DevGo Sr"
            salary:        "R$ 18k – R$ 25k"
        }
    }),
    
    (#OutreachTest & {
        id:          4
        prompt:      "Follow-up Day 4 para Rafael (sem resposta)"
        messageType: "Followup"
        expected: {
            candidateName: "Rafael"
            jobTitle:      "Go Senior"
            salary:        ""
        }
    }),
    
    (#OutreachTest & {
        id:          5
        prompt:      "Follow-up Day 7 para Ana (sem resposta final)"
        messageType: "Followup"
        expected: {
            candidateName: "Ana"
            jobTitle:      "Tech Lead Java"
            salary:        ""
        }
    }),
]
