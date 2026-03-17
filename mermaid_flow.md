graph TD

    %% Styles
    classDef database fill:#E8F1FF,stroke:#2B6CB0,stroke-width:2px,color:#1A365D;
    classDef gui fill:#E6FFFA,stroke:#2C7A7B,stroke-width:2px,color:#234E52;
    classDef bots fill:#FFF5E6,stroke:#C05621,stroke-width:2px,color:#7B341E;
    classDef user fill:#F7FAFC,stroke:#4A5568,stroke-width:2px,color:#1A202C;

    subgraph UserInterface
        GUI[Dashboard GUI / Client Detail Page]
        CRUD[Generic CRUD Engine / DRF API]
        Forms[Generic Forms View]
    end

    subgraph CentralDatabase
        Clients[(Client Table: apps_clients_client)]
        BotStatus[(Bot Status Table: crud_gui_dashboard_bots)]
        BotRecords[(Execution Records: crud_gui_dashboard_records_2)]
        History[(Audit Logs: simple_history)]
    end

    subgraph BotWorkers
        BotA[Bot Worker 1]
        BotB[Bot Worker 2]
    end

    User([Admin / Editor User])

    User <-->|HTTPS| GUI

    GUI <--> CRUD

    CRUD -->|Django ORM| Clients
    CRUD -->|Django ORM| BotStatus
    CRUD -->|Django ORM| BotRecords
    CRUD -->|Django ORM| History

    BotA -->|Fetch Clients| Clients
    BotB -->|Fetch Clients| Clients

    BotA -->|Heartbeat| BotStatus
    BotB -->|Heartbeat| BotStatus

    BotA -->|Log Result bank_rel link| BotRecords
    BotB -->|Log Result bank_rel link| BotRecords

    BotRecords -.->|client_uuid link| Clients

    class Clients,BotStatus,BotRecords,History database
    class GUI,CRUD,Forms gui
    class BotA,BotB bots
    class User user