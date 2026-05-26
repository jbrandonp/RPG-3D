-- Table quests_progress (progression quêtes)
CREATE TABLE quests_progress (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    character_id UUID NOT NULL REFERENCES characters(id) ON DELETE CASCADE,
    quest_id    VARCHAR(100) NOT NULL,
    state       VARCHAR(50) DEFAULT 'active',
    current_step SMALLINT DEFAULT 0,
    kill_count  INT DEFAULT 0,
    updated_at  TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(character_id, quest_id)
);
