```mermaid
erDiagram
    TRIDA ||--o{ ZAK : "obsahuje"
    ZAK ||--o{ ZAPSANI : "má"
    KROUZEK ||--o{ ZAPSANI : "navštěvuje"

    TRIDA {
        int id PK
        string nazev
    }
    ZAK {
        int id PK
        string jmeno
        string prijmeni
        int trida_id FK
    }
    KROUZEK {
        int id PK
        string nazev
    }
    ZAPSANI {
        int zak_id PK, FK
        int krouzek_id PK, FK
        date datum_zapsani
    }
    ```