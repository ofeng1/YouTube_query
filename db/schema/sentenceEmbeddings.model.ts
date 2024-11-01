import { index, integer, pgTable, serial, timestamp } from "drizzle-orm/pg-core";
import { pgVector, tsVector } from "./types";
import { videos } from "./videos.model";
import { sentences } from "./sentences.model";

export const sentenceEmbeddings = pgTable(
  "sentence_embeddings",
  {
    id: serial("id").primaryKey().notNull(),
    createdAt: timestamp("createdAt").defaultNow().notNull(),
    sentenceId: integer("sentence_id")
      .notNull()
      .references(() => sentences.id, {
        onDelete: "cascade",
        onUpdate: "cascade",
      }),
    videoId: integer("video_id")
      .notNull()
      .references(() => videos.id, {
        onDelete: "cascade",
        onUpdate: "cascade",
      }),
    embedding: pgVector("embedding", 1536),
    fulltext: tsVector("fulltext"),
  },
  (table) => {
    return {
      fulltextIdx: index("PassageEmbedding_fulltext_idx").on(table.fulltext),
    };
  },
);
