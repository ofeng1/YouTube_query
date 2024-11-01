import { text, integer, pgTable, serial, timestamp } from "drizzle-orm/pg-core";
import { videos } from "./videos.model";

export const sentences = pgTable("sentences", {
  id: serial("id").primaryKey().notNull(),
  createdAt: timestamp("createdAt").defaultNow().notNull(),
  content: text("content").notNull(),
  videoId: integer("video_id")
    .notNull()
    .references(() => videos.id, {
      onDelete: "cascade",
      onUpdate: "cascade",
    }),
});
