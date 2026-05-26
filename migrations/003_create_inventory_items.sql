-- Table inventory_items (inventaire)
CREATE TABLE inventory_items (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    character_id UUID NOT NULL REFERENCES characters(id) ON DELETE CASCADE,
    item_id     VARCHAR(100) NOT NULL,
    quantity    INT DEFAULT 1,
    slot        SMALLINT,
    durability  SMALLINT DEFAULT 100,
    enhancement_level SMALLINT DEFAULT 0,
    is_equipped BOOLEAN DEFAULT FALSE,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);
