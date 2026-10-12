SP1 Kroužky
13
1. nadbytečné opakování dat: Informace o jednotlivých kroužcích (vedoucí, den, čas, místnost a cena) se zbytečně opakují na každém. Pokud by se například změnila místnost nebo vedoucí kroužku, musel by se tento údaj opravovat na mnoha místech.
2.Nejednotnost a nekonzistentnost zápisu: Stejné hodnoty jsou v různých řádcích zapsány odlišně (např. kroužek Robotika, robotika, ROBOTIKA; dny čt vs. čtvrtek; jména vedoucích Mgr. Horák, Horák, Horak).
3.Neschopnost spolehlivě odpovídat na dotazy: Z tabulky nelze bez ručního prohledávání a čištění dat spolehlivě zjistit základní informace, jako je přesný počet nabízených kroužků nebo celková vybraná částka na poplatcích, protože vyhledávání selže na překlepách a smíšených datových typech.
2. Primární a cizí klíče zaci: PK `id_zaka` pak krouzky: PK `id_krouzku` pak prihlasky: PK `id_prihlasky`, FK `id_zaka` → `zaci`, FK `id_krouzku` → `krouzky`
3. ## 4. ER Diagram

erDiagram
    ZAK ||--o{ PRIHLASKA : "přihlašuje se"
    KROUZEK ||--o{ PRIHLASKA : "obsahuje"

    ZAK {
        int id_zaka PK
        string jmeno
        string prijmeni
        string trida
    }

    KROUZEK {
        int id_krouzku PK
        string nazev
        string vedouci
        string den
        string cas
        string mistnost
        int cena_kc
    }

    PRIHLASKA {
        int id_prihlasky PK
        int id_zaka FK
        int id_krouzku FK
        string zaplaceno
    }
    
4. SELECT nazev, cena_kc
FROM krouzky
WHERE cena_kc > 500;