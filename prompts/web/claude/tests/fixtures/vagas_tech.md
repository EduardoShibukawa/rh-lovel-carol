# Fixture: Vagas Tech (Múltiplas vagas)

**Formato:** Multi-vaga Lovel  
**Skill Alvo:** post, hunting

## Entrada

```
Desenvolvedor Senior C# .Net R$10000K - R$14000K Hybrid | São Paulo (SP) | PJ | Senior 
Desenvolvedor .Net Fullstack R$9000K - R$12000K Hybrid | São Paulo (SP) | CLT | Senior 
Engenheiro De Software Senior R$15000K - R$20000K Presential | Niterói (RJ) | PJ | Senior 
Tech Lead R$15000K - R$18000K Hybrid | São Paulo (SP) | PJ | Senior
```

## Expected Output (POST)

### Hooks de Impacto (Lou Adler)
- BOM: "Tornar API 3x mais rápida em 90 dias" (se dado da vaga)
- BOM: "Escalar sistemas para 100k+ usuários"
- BOM: "Liderar equipe de engenheiros"

### Estrutura
```
🚀 [Hook de impacto]
💰 [Faixa] | [CLT/PJ] | [Senioridade]
📍 [Modelo] | [Cidade]
🛠️ [Stack]
🔗 [Link com invite]
```

## Expected Output (HUNTING)

### Boolean Query
```
("C#" OR ".NET" OR ".Net" OR "C Sharp" OR "DotNET")
AND (developer OR engineer OR "software engineer" OR programmer)
AND ("São Paulo" OR "SP" OR "Região Metropolitana de São Paulo")
NOT (júnior OR junior OR trainee OR estagio OR aprendiz)
```

### X-Ray
```
site:linkedin.com/in/ "C#" OR ".NET" "São Paulo" -"open to work"
```
