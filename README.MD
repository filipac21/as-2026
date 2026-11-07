# Aplikační software — IT2, 2026/27

Repozitář pro předmět AS (databáze). Sem ukládám všechna cvičení
za celý školní rok. Odevzdává se commitem, ne mailem.

## Struktura

- `2026-09/` — září: Git, první data
- `2026-10/` — říjen: relační model
- (další měsíce přibudou)

```mermaid
erDiagram
    ZAKAZNIK ||--o{ OBJEDNAVKA : "zadává"
    OBJEDNAVKA ||--|{ POLOZKA : "obsahuje"
    PRODUKT ||--o{ POLOZKA : "je v"

    ZAKAZNIK {
        int id PK
        string jmeno
        string prijmeni
        string mesto
        string email
    }
    OBJEDNAVKA {
        int cislo PK
        date datum
        int id_zakaznika FK
    }
    PRODUKT {
        int id PK
        string nazev
        int cena
    }
    POLOZKA {
        int id_objednavky PK
        int id_produktu PK
        int pocet
    }
