SELECT ki.*, c.embedding
FROM chunks c
JOIN knowledge_items ki ON c.knowledge_item_id = ki.id
JOIN knowledge_item_tags kit ON kit.knowledge_item_id = ki.id
JOIN tags t ON kit.tag_id = t.id
WHERE t.name = 'nutrition'
ORDER BY c.embedding <=> '[your_query_vector]'
LIMIT 10;
