-- Index sur vraies requêtes fréquentes uniquement
CREATE INDEX idx_characters_user_id ON characters(user_id);
CREATE INDEX idx_inventory_character_id ON inventory_items(character_id);
CREATE INDEX idx_quests_character_id ON quests_progress(character_id);
CREATE INDEX idx_transactions_from_char ON transactions(from_char);
CREATE INDEX idx_transactions_to_char ON transactions(to_char);
CREATE INDEX idx_characters_zone ON characters(zone_id);
