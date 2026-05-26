-- Table transactions (économie — atomique)
CREATE TABLE transactions (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    from_char   UUID REFERENCES characters(id),
    to_char     UUID REFERENCES characters(id),
    item_id     VARCHAR(100),
    quantity    INT,
    gold_amount BIGINT DEFAULT 0,
    tx_type     VARCHAR(50) NOT NULL,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);
