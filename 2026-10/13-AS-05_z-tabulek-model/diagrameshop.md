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