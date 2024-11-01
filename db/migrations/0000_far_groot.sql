CREATE TABLE IF NOT EXISTS "sentence_embeddings" (
	"id" serial PRIMARY KEY NOT NULL,
	"createdAt" timestamp DEFAULT now() NOT NULL,
	"embedding" "vector(1536)",
	"fulltext" "tsvector"
);
--> statement-breakpoint
CREATE INDEX IF NOT EXISTS "PassageEmbedding_fulltext_idx" ON "sentence_embeddings" ("fulltext");