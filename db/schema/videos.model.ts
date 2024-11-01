import { text, pgTable, serial, timestamp } from "drizzle-orm/pg-core";

export const videos = pgTable("videos", {
  id: serial("id").primaryKey().notNull(),
  createdAt: timestamp("createdAt").defaultNow().notNull(),
  link: text("link").unique().notNull(),
});
